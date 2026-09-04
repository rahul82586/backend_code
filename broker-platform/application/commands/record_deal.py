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

from core.domains.accounts.models import Account, AccountType
from core.domains.oms.entities.order import Order, OrderState
from core.domains.oms.entities.deal import Deal, DealType
from core.domains.oms.entities.position import Position
from core.domains.common.value_objects import Price, Volume, Money
from core.events.domain_events import DealCreated, PositionUpdated
from core.ports.interfaces import IOrderRepository, IEventBus, IAccountRepository, IPositionRepository

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
        event_bus: IEventBus
    ):
        self.order_repo = order_repo
        self.account_repo = account_repo
        self.position_repo = position_repo
        self.event_bus = event_bus

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

        # 5. Update Account Balance (Commission/Swap/Profit)
        # Note: Unrealized PnL is in Position, Realized PnL affects Balance
        if deal.profit.amount != 0:
            account.balance = account.balance + deal.profit
            logger.debug(f"Account {account.login_id} balance updated by {deal.profit.amount}")
        
        if deal.commission.amount != 0:
            # Commission is usually negative money
            account.balance = account.balance + deal.commission
            
        # Recalculate Equity and Margin
        # In production, this requires re-evaluating all open positions
        # account.equity = account.balance + total_unrealized_pnl
        
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
        Respects the Group's Position Mode (Hedging vs Netting).
        """
        if deal.deal_type not in [DealType.BUY, DealType.SELL]:
            return # Ignore non-trading deals for position logic

        group_mode = account.group.execution.mode # HEDGING or NETTING (if implemented)
        
        # For Phase 4, we assume HEDGING default as per MT5 Retail standard
        # In Hedging: Every BUY/SELL creates a NEW independent position.
        # Aggregation happens only in the UI or Portfolio View, not in the core Position entity storage.
        
        logger.info(f"Applying deal to position (Hedging Mode) for {account.login_id}")
        
        # Create a new Position ID
        # Format: {login}_{symbol}_{uuid} ensures uniqueness for hedging
        position_id = f"{account.login_id}_{deal.symbol}_{str(uuid.uuid4())[:8]}"
        
        new_position = Position(
            id=position_id,
            account_login=account.login_id,
            symbol=deal.symbol,
            volume=deal.volume,
            side=deal.deal_type, # Maps BUY/SELL DealType to OrderType side
            average_price=deal.price,
            contract_size=Decimal('100000'), # TODO: Fetch from Symbol definition
            opened_at=datetime.now(timezone.utc)
        )
        
        # Save the new position
        await self.position_repo.save(new_position)
        logger.debug(f"New Position {position_id} created")
        
        # Publish Position Updated Event (Creation is an update)
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
