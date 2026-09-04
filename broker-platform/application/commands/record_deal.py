"""
Record Deal Command Handler.
Triggered when a match occurs (Internal Engine or External LP Fill).
Updates Positions, Balances, and publishes Deal events.
"""
import logging
from dataclasses import dataclass
from datetime import datetime, timezone
from decimal import Decimal
from typing import List, Optional
import uuid

from core.domains.accounts.models import Account, AccountType, ExecutionMode
from core.domains.oms.entities.order import Order, OrderState, OrderType
from core.domains.oms.entities.deal import Deal, DealType
from core.domains.oms.entities.position import Position
from core.domains.common.value_objects import Price, Volume, Money
from core.events.domain_events import DealCreated, PositionUpdated
from core.ports.interfaces import IOrderRepository, IEventBus, IAccountRepository, IPositionRepository, ISymbolRepository, IMarketDataFeed

logger = logging.getLogger(__name__)


@dataclass
class RecordDealCommand:
    """
    Command to record an execution (fill).
    Triggered by the Matching Engine or Liquidity Gateway.
    """
    order_id: str
    account_login: str
    symbol: str
    volume: Decimal
    price: Decimal
    deal_type: DealType  # BUY, SELL, SWAP, COMMISSION
    commission_amount: Decimal = Decimal('0')
    swap_amount: Decimal = Decimal('0')
    profit: Decimal = Decimal('0')
    external_deal_id: Optional[str] = None  # ID from LP (e.g., LMAX, Binance)


class RecordDealHandler:
    """
    Handler for recording trades.
    
    Architectural Purpose:
    This is the critical 'Write' path for trade execution. It ensures 
    atomicity of the 'Deal -> Position -> Balance' update sequence.
    In a real system, this entire method should run inside a DB Transaction.
    """
    
    def __init__(
        self,
        order_repo: IOrderRepository,
        account_repo: IAccountRepository,
        position_repo: IPositionRepository,
        event_bus: IEventBus,
        symbol_repo: ISymbolRepository,
        market_feed: IMarketDataFeed
    ):
        self.order_repo = order_repo
        self.account_repo = account_repo
        self.position_repo = position_repo
        self.event_bus = event_bus
        self.symbol_repo = symbol_repo
        self.market_feed = market_feed

    async def execute(self, command: RecordDealCommand) -> Deal:
        logger.info(f"Recording Deal for Order {command.order_id}, Volume {command.volume}")
        
        # 1. Fetch and Update Order
        order = await self.order_repo.find_by_id(command.order_id)
        if not order:
            raise ValueError(f"Order {command.order_id} not found")
        
        # Apply fill to order (updates state to FILLED or PARTIALLY_FILLED)
        volume_obj = Volume(Decimal(str(command.volume)))
        price_obj = Price(Decimal(str(command.price)))
        
        try:
            order.apply_fill(volume_obj, price_obj)
        except ValueError as e:
            logger.error(f"Failed to apply fill to order {order.ticket_id}: {e}")
            raise
        
        await self.order_repo.save(order)

        # 2. Create Immutable Deal Entity
        deal_id = str(uuid.uuid4()) # Or sequential from DB
        deal = Deal(
            deal_id=deal_id,
            order_id=command.order_id,
            account_login=command.account_login,
            symbol=command.symbol,
            deal_type=command.deal_type,
            volume=volume_obj,
            price=price_obj,
            commission=Money(Decimal(str(command.commission_amount)), "USD"),
            swap=Money(Decimal(str(command.swap_amount)), "USD"),
            profit=Money(Decimal(str(command.profit)), "USD"),
            created_at=datetime.now(timezone.utc)
        )
        
        # TODO: Save Deal to Repository (Append-only log)
        # await self.deal_repo.save(deal)

        # 3. Fetch Account
        account = await self.account_repo.find_by_login(command.account_login)
        if not account:
            raise ValueError(f"Account {command.account_login} not found")

        # 4. Apply Deal to Position(s)
        # Logic depends on Group Position Mode (Hedging vs Netting)
        await self._apply_deal_to_positions(account, deal)

        # 5. Update Account Balance (Commission/Swap/Profit) AND Margin
        # Note: Unrealized PnL is in Position, Realized PnL affects Balance
        if deal.profit.amount != 0:
            account.balance = account.balance + deal.profit
            logger.debug(f"Account {account.login_id} balance updated by {deal.profit.amount}")
        
        if deal.commission.amount != 0:
            # Commission is usually negative money
            account.balance = account.balance + deal.commission
        
        # CRITICAL FIX: Recalculate Margin Used and Free Margin after deal execution
        # Opening a trade must freeze margin; closing must release it
        await self._recalculate_account_margin(account)
        
        await self.account_repo.save(account)

        # 6. Publish Event
        event = DealCreated(
            aggregate_id=deal.deal_id,
            payload={
                "deal_id": deal.deal_id,
                "order_id": deal.order_id,
                "account_login": deal.account_login,
                "symbol": deal.symbol,
                "type": deal.deal_type.value,
                "volume": str(deal.volume.value),
                "price": str(deal.price.value),
                "commission": str(deal.commission.amount),
                "profit": str(deal.profit.amount)
            }
        )
        await self.event_bus.publish(event)
        logger.info(f"Deal {deal.deal_id} recorded and event published")

        return deal

    async def _apply_deal_to_positions(self, account: Account, deal: Deal):
        """
        Handles the complex logic of updating positions based on Deal type.
        Respects the Group's Position Mode (HEDGING vs NETTING).
        """
        if deal.deal_type not in [DealType.BUY, DealType.SELL]:
            return  # Ignore non-trading deals for position logic

        group_mode = account.group.execution.mode  # HEDGING or NETTING
        
        logger.info(f"Applying deal to position ({group_mode.value} Mode) for {account.login_id}")
        
        # Fetch symbol for contract size
        symbol = await self.symbol_repo.find_by_name(deal.symbol)
        if not symbol:
            raise ValueError(f"Symbol {deal.symbol} not found for position calculation")
        
        if group_mode == ExecutionMode.EXCHANGE or group_mode.name == "NETTING":
            # NETTING MODE: Opposite deals reduce/close existing positions
            await self._apply_deal_netting_mode(account, deal, symbol)
        else:
            # HEDGING MODE (Default MT5 Retail): Every deal creates a new independent position
            await self._apply_deal_hedging_mode(account, deal, symbol)

    async def _apply_deal_hedging_mode(self, account: Account, deal: Deal, symbol):
        """Hedging: Every BUY/SELL creates a NEW independent position."""
        position_id = f"{account.login_id}_{deal.symbol}_{str(uuid.uuid4())[:8]}"
        
        new_position = Position(
            id=position_id,
            account_login=account.login_id,
            symbol=deal.symbol,
            volume=deal.volume,
            side=deal.deal_type,
            average_price=deal.price,
            contract_size=symbol.contract_size,
            opened_at=datetime.now(timezone.utc)
        )
        
        await self.position_repo.save(new_position)
        logger.debug(f"New Position {position_id} created (Hedging)")
        
        evt = PositionUpdated(
            aggregate_id=position_id,
            payload={
                "position_id": position_id,
                "account_login": account.login_id,
                "symbol": deal.symbol,
                "volume": str(new_position.volume.value),
                "side": new_position.side.value,
                "action": "OPENED"
            }
        )
        await self.event_bus.publish(evt)

    async def _apply_deal_netting_mode(self, account: Account, deal: Deal, symbol):
        """
        Netting: Opposite deals reduce/close existing positions.
        Same direction adds to position.
        """
        deal_side = OrderType.BUY if deal.deal_type == DealType.BUY else OrderType.SELL
        
        # Find existing position for this symbol and side
        existing_positions = await self.position_repo.find_by_account_and_symbol(
            account.login_id, 
            deal.symbol
        )
        
        # Filter for same side positions (in netting there should be only one per symbol)
        matching_position = None
        for pos in existing_positions:
            if pos.side == deal_side:
                matching_position = pos
                break
        
        if matching_position:
            # Same direction: Add to position
            if deal_side == matching_position.side:
                total_val = (matching_position.average_price.value * matching_position.volume.value) + \
                           (deal.price.value * deal.volume.value)
                new_vol = matching_position.volume.value + deal.volume.value
                matching_position.volume = Volume(new_vol)
                matching_position.average_price = Price(total_val / new_vol)
                await self.position_repo.save(matching_position)
                logger.debug(f"Position {matching_position.id} increased (Netting)")
        else:
            # No existing position or opposite side: Create new or reverse
            # Check for opposite position to close/reverse
            opposite_positions = [p for p in existing_positions if p.side != deal_side]
            
            if opposite_positions:
                opp_pos = opposite_positions[0]
                # Close partial/full or reverse
                if deal.volume.value < opp_pos.volume.value:
                    # Partial close - reduce volume
                    opp_pos.volume = Volume(opp_pos.volume.value - deal.volume.value)
                    await self.position_repo.save(opp_pos)
                    logger.debug(f"Position {opp_pos.id} partially closed (Netting)")
                elif deal.volume.value == opp_pos.volume.value:
                    # Full close - remove position
                    await self.position_repo.delete(opp_pos.id)
                    logger.debug(f"Position {opp_pos.id} fully closed (Netting)")
                else:
                    # Reverse - close old and create new
                    await self.position_repo.delete(opp_pos.id)
                    position_id = f"{account.login_id}_{deal.symbol}_{str(uuid.uuid4())[:8]}"
                    new_vol = deal.volume.value - opp_pos.volume.value
                    new_position = Position(
                        id=position_id,
                        account_login=account.login_id,
                        symbol=deal.symbol,
                        volume=Volume(new_vol),
                        side=deal_side,
                        average_price=deal.price,
                        contract_size=symbol.contract_size,
                        opened_at=datetime.now(timezone.utc)
                    )
                    await self.position_repo.save(new_position)
                    logger.debug(f"Position reversed (Netting)")
            else:
                # No existing position at all - create new
                position_id = f"{account.login_id}_{deal.symbol}_{str(uuid.uuid4())[:8]}"
                new_position = Position(
                    id=position_id,
                    account_login=account.login_id,
                    symbol=deal.symbol,
                    volume=deal.volume,
                    side=deal_side,
                    average_price=deal.price,
                    contract_size=symbol.contract_size,
                    opened_at=datetime.now(timezone.utc)
                )
                await self.position_repo.save(new_position)
                logger.debug(f"New Position {position_id} created (Netting)")

    async def _recalculate_account_margin(self, account: Account):
        """
        Recalculates margin_used and margin_free based on all open positions.
        Formula: Sum(Position.Volume * ContractSize * CurrentPrice) / Leverage
        """
        # Fetch all open positions for this account
        all_positions = await self.position_repo.find_by_account(account.login_id)
        
        total_margin_used = Decimal('0')
        
        for position in all_positions:
            if position.volume.value == 0:
                continue  # Skip closed positions
            
            # Fetch current market price for unrealized PnL and margin calc
            tick = await self.market_feed.get_latest_tick(position.symbol)
            
            # Use position's average price as fallback if no tick available
            current_price = Decimal(tick['ask']) if tick else position.average_price.value
            
            # Get symbol for contract size and margin %
            symbol = await self.symbol_repo.find_by_name(position.symbol)
            if not symbol:
                continue
            
            # Calculate margin for this position
            position_margin = symbol.calculate_margin_required(
                position.volume.value, 
                current_price
            )
            total_margin_used += position_margin
        
        # Update account margin fields
        currency = account.balance.currency
        account.margin_used = Money(total_margin_used, currency)
        account.margin_free = Money(account.balance.amount - total_margin_used, currency)
        
        logger.debug(
            f"Account {account.login_id} margin recalculated: "
            f"Used={total_margin_used}, Free={account.margin_free.amount}"
        )
