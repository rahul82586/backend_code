"""
Create Order Command Handler.
Orchestrates the flow of creating a new order: Validation -> Persistence -> Event Publishing.
"""
import logging
from dataclasses import dataclass
from datetime import datetime, timezone
from decimal import Decimal
from typing import Optional

from core.domains.accounts.models import Account
from core.domains.instruments.models import Symbol
from core.domains.oms.entities.order import Order, OrderType, OrderState
from core.domains.common.value_objects import Price, Volume, Money
from core.events.domain_events import OrderCreated
from core.ports.interfaces import IOrderRepository, IEventBus, IAccountRepository, IMarketDataFeed

from application.services.risk_service import PreTradeRiskService

logger = logging.getLogger(__name__)


@dataclass
class CreateOrderCommand:
    """
    Data transfer object for creating an order.
    Contains all necessary fields to construct an Order entity.
    """
    account_login: str
    symbol: str
    order_type: OrderType
    volume: Decimal
    price: Optional[Decimal] = None  # None for Market Orders
    stop_loss: Optional[Decimal] = None
    take_profit: Optional[Decimal] = None
    comment: str = ""


class CreateOrderHandler:
    """
    Command Handler for CreateOrderCommand.
    
    Architectural Purpose:
    Implements the CQRS 'Command' side. It contains the application logic 
    (orchestration) but delegates business rules to the Domain Entities 
    and Risk Service. It relies strictly on Ports (Interfaces), not 
    concrete Infrastructure implementations.
    """
    
    def __init__(
        self,
        order_repo: IOrderRepository,
        account_repo: IAccountRepository,
        market_feed: IMarketDataFeed,
        event_bus: IEventBus
    ):
        self.order_repo = order_repo
        self.account_repo = account_repo
        self.market_feed = market_feed
        self.event_bus = event_bus
        self.risk_service = PreTradeRiskService(event_bus)

    async def execute(self, command: CreateOrderCommand) -> Order:
        """
        Executes the order creation workflow.
        1. Fetch Account & Group
        2. Fetch Symbol Definition
        3. Get Current Price (for Market orders or validation)
        4. Run Pre-Trade Risk Checks
        5. Construct Order Entity
        6. Persist Order
        7. Publish Event
        """
        logger.info(f"Processing CreateOrderCommand for {command.account_login} on {command.symbol}")
        
        # 1. Fetch Account
        account = await self.account_repo.find_by_login(command.account_login)
        if not account:
            raise ValueError(f"Account {command.account_login} not found")
        
        if not account.can_trade():
            raise PermissionError(f"Account {command.account_login} is not allowed to trade")

        # 2. Fetch Symbol
        # In production, this might come from a cached instrument service
        symbol = await self._get_symbol_definition(command.symbol)
        if not symbol:
            raise ValueError(f"Symbol {command.symbol} not found")
        if not symbol.is_trade_allowed:
            raise ValueError(f"Symbol {command.symbol} trading is suspended")

        # 3. Determine Execution Price
        # If Market Order, fetch current ask/bid. If Limit, use provided price.
        execution_price = command.price
        if command.price is None:
            # Market Order: Need current price for margin check and slippage estimation
            tick = await self.market_feed.get_latest_tick(command.symbol)
            if not tick:
                raise RuntimeError(f"No market data available for {command.symbol}")
            
            # Simple logic: Buy uses Ask, Sell uses Bid
            if command.order_type in [OrderType.BUY, OrderType.BUY_LIMIT, OrderType.BUY_STOP]:
                execution_price = float(tick['ask'])
            else:
                execution_price = float(tick['bid'])
        
        price_obj = Price(Decimal(str(execution_price)))
        volume_obj = Volume(Decimal(str(command.volume)))

        # 4. Construct Order Entity (Transient)
        ticket_id = await self.order_repo.get_next_ticket_id()
        order = Order(
            ticket_id=ticket_id,
            account_login=command.account_login,
            symbol=command.symbol,
            order_type=command.order_type,
            volume=volume_obj,
            price=price_obj,
            stop_loss=Price(Decimal(str(command.stop_loss))) if command.stop_loss else None,
            take_profit=Price(Decimal(str(command.take_profit))) if command.take_profit else None,
            state=OrderState.NEW,
            created_at=datetime.now(timezone.utc),
            updated_at=datetime.now(timezone.utc)
        )

        # 5. Pre-Trade Risk Check (The Gatekeeper)
        is_approved = await self.risk_service.validate_order(
            order=order,
            account=account,
            symbol=symbol,
            current_price=price_obj
        )
        
        if not is_approved:
            # Risk service already published Rejection event
            logger.warning(f"Order {ticket_id} rejected by risk service")
            raise PermissionError("Order rejected by pre-trade risk checks")

        # 6. Persist Order
        # State changes to PLACED upon successful save
        order.state = OrderState.PLACED
        saved_order = await self.order_repo.save(order)
        logger.info(f"Order {saved_order.ticket_id} persisted successfully")

        # 7. Publish Domain Event
        # This triggers downstream processes: Matching Engine, Dealer UI, Analytics
        event = OrderCreated(
            aggregate_id=saved_order.ticket_id,
            payload={
                "ticket_id": saved_order.ticket_id,
                "account_login": saved_order.account_login,
                "symbol": saved_order.symbol,
                "type": saved_order.order_type.value,
                "volume": str(saved_order.volume.value),
                "price": str(saved_order.price.value) if saved_order.price else None,
                "state": saved_order.state.value
            }
        )
        await self.event_bus.publish(event)
        logger.debug(f"OrderCreated event published for {saved_order.ticket_id}")

        return saved_order

    async def _get_symbol_definition(self, symbol_name: str) -> Optional[Symbol]:
        """
        Helper to fetch symbol definition.
        In a real app, this would use an IInstrumentRepository port.
        For now, we simulate it or assume a static lookup.
        """
        # TODO: Inject IInstrumentRepository in __init__ and use it here
        # Placeholder implementation
        logger.warning("Symbol lookup placeholder implemented. Inject IInstrumentRepository for production.")
        return None 
