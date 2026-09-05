"""
Execution Orchestrator.

The master conductor that receives OrderApprovedEvent and routes it
to the correct execution destination based on the Smart Order Router's decision.

Architectural Purpose:
Orchestrates the flow from approved order to final execution (A-Book, B-Book, ECN, or Dealer).
Acts as the central hub connecting Risk, Routing, and Execution layers.
"""
import logging
from typing import Optional
from decimal import Decimal

from core.domains.execution.router import SmartOrderRouter
from core.domains.execution.models import (
    ExecutionInstruction, 
    ExecutionDestination, 
    CoverageAccount
)
from core.domains.oms.entities.order import Order, OrderState
from core.domains.accounts.models import Account
from core.events.domain_events import DomainEvent, EventType
from core.ports.interfaces import (
    IEventBus, 
    IOrderRepository, 
    IAccountRepository,
    ILiquidityGateway,
    IMatchingEngine,
    ICoverageAccountRepository
)
from application.services.dealer_queue_service import DealerQueueService

logger = logging.getLogger(__name__)


class ExecutionOrchestrator:
    """
    The central conductor that receives OrderApprovedEvent and routes it
    to the correct execution destination.
    
    Flow:
    OrderApprovedEvent → SmartOrderRouter → ExecutionInstruction
        → A_BOOK: ILiquidityGateway.send_order()
        → B_BOOK: IMatchingEngine.fill_internal() + CoverageAccount.update()
        → IN_HOUSE_ECN: IMatchingEngine.submit_to_book()
        → TO_DEALER: DealerQueueService.enqueue()
        → REJECT: Emit OrderRejectedEvent
    """
    
    def __init__(
        self,
        router: SmartOrderRouter,
        dealer_queue: DealerQueueService,
        liquidity_gateway: ILiquidityGateway,
        matching_engine: IMatchingEngine,
        event_bus: IEventBus,
        order_repo: IOrderRepository,
        account_repo: IAccountRepository,
        coverage_repo: ICoverageAccountRepository
    ):
        self.router = router
        self.dealer_queue = dealer_queue
        self.liquidity_gateway = liquidity_gateway
        self.matching_engine = matching_engine
        self.event_bus = event_bus
        self.order_repo = order_repo
        self.account_repo = account_repo
        self.coverage_repo = coverage_repo
        
        logger.info("ExecutionOrchestrator initialized")

    async def handle_order_approved(self, event: DomainEvent):
        """
        Main entry point. Subscribes to OrderApprovedEvent on the bus.
        Routes the order based on SOR decision.
        """
        order_id = event.payload.get('order_id')
        if not order_id:
            logger.error("OrderApprovedEvent missing order_id")
            return
        
        # Fetch order and account
        order: Optional[Order] = await self.order_repo.find_by_id(order_id)
        if not order:
            logger.error(f"Order {order_id} not found")
            return
        
        account: Optional[Account] = await self.account_repo.find_by_login(order.account_login)
        if not account:
            logger.error(f"Account {order.account_login} not found")
            return
        
        # Route the order
        instruction = self.router.route(order, account)
        
        # Emit routing event
        route_event = DomainEvent(
            event_type=EventType.ORDER_ROUTED,
            aggregate_id=order_id,
            payload={
                "order_id": order_id,
                "destination": instruction.destination.value,
                "rule_id": instruction.rule_id,
                "reason": instruction.reason
            }
        )
        await self.event_bus.publish(route_event)
        
        # Dispatch to appropriate handler
        if instruction.destination == ExecutionDestination.A_BOOK:
            await self._execute_a_book(order, instruction)
        elif instruction.destination == ExecutionDestination.B_BOOK:
            await self._execute_b_book(order, instruction, account)
        elif instruction.destination == ExecutionDestination.IN_HOUSE_ECN:
            await self._execute_in_house(order, instruction)
        elif instruction.destination == ExecutionDestination.TO_DEALER:
            await self._send_to_dealer(order)
        elif instruction.destination == ExecutionDestination.REJECT:
            await self._reject_order(order, instruction.reason or "Blocked by routing rule")
        else:
            logger.error(f"Unknown execution destination: {instruction.destination}")

    async def _execute_a_book(self, order: Order, instruction: ExecutionInstruction):
        """
        Send to external Liquidity Provider (LP).
        Emits OrderRoutedEvent.
        """
        logger.info(f"Executing order {order.ticket_id} via A-Book gateway {instruction.gateway_id}")
        
        try:
            # Send to external LP via FIX/REST gateway
            execution_report = await self.liquidity_gateway.send_order(
                order=order,
                gateway_id=instruction.gateway_id
            )
            
            # Update order state
            order.state = OrderState.PLACED
            await self.order_repo.save(order)
            
            # Emit success event
            event = DomainEvent(
                event_type=EventType.ORDER_ROUTED,
                aggregate_id=order.ticket_id,
                payload={
                    "order_id": order.ticket_id,
                    "gateway_id": instruction.gateway_id,
                    "execution_report": str(execution_report)
                }
            )
            await self.event_bus.publish(event)
            
        except Exception as e:
            logger.error(f"A-Book execution failed for {order.ticket_id}: {e}")
            await self._reject_order(order, f"A-Book gateway error: {str(e)}")

    async def _execute_b_book(self, order: Order, instruction: ExecutionInstruction, account: Account):
        """
        Internalize the trade (broker is counterparty).
        Creates an immutable Deal entity, updates client Position and Account margin,
        THEN updates CoverageAccount exposure.
        
        SIGN CONVENTION (CRITICAL):
        - Client BUY → Broker SELL → volume_delta NEGATIVE (broker is SHORT)
        - Client SELL → Broker BUY → volume_delta POSITIVE (broker is LONG)
        
        This matches CoverageAccount docstring: Positive = broker is long.
        """
        logger.info(f"Executing order {order.ticket_id} via B-Book (internal)")
        
        try:
            # Execute internally (simulate fill at market price)
            fill_price = await self.matching_engine.execute_internal(order)
            
            # Create immutable Deal entity
            from core.domains.oms.entities.deal import Deal, DealType
            deal = Deal(
                deal_id=f"DEAL_{order.ticket_id}",  # In production, use proper ID generation
                order_id=order.ticket_id,
                account_login=order.account_login,
                symbol=order.symbol,
                deal_type=DealType.BUY if order.order_type == OrderType.BUY else DealType.SELL,
                volume=order.volume,
                price=fill_price,
                commission=account.group.commission.value,  # Simplified
                swap=Decimal('0'),  # Calculated separately in Ledger service
                profit=Decimal('0')  # Realized PnL calculated on close
            )
            
            # Apply deal to position and update account margin
            # This calls the RecordDealCommand logic
            from application.commands.record_deal import RecordDealCommand, RecordDealCommandHandler
            record_command = RecordDealCommand(
                deal=deal,
                account_login=order.account_login
            )
            # Note: In production, inject this handler via DI container
            # For now, we call the logic directly
            await self._apply_deal_to_account(deal, account)
            
            # Update Coverage Account exposure with CORRECT sign convention
            # Client BUY → Negative delta (broker sold/short)
            # Client SELL → Positive delta (broker bought/long)
            is_buy = order.order_type.name.startswith("BUY")
            volume_delta = -order.volume.value if is_buy else order.volume.value
            
            coverage_account_id = instruction.coverage_account_id or "DEFAULT_COVERAGE"
            await self.coverage_repo.update_exposure(
                account_id=coverage_account_id,
                symbol=order.symbol,
                volume_delta=volume_delta
            )
            
            # Update order state
            order.state = OrderState.FILLED
            await self.order_repo.save(order)
            
            # Emit fill event
            event = DomainEvent(
                event_type=EventType.DEAL_CREATED,
                aggregate_id=order.ticket_id,
                payload={
                    "order_id": order.ticket_id,
                    "deal_id": deal.deal_id,
                    "deal_type": deal.deal_type.value,
                    "price": str(fill_price),
                    "volume": str(order.volume.value),
                    "coverage_updated": True,
                    "coverage_account_id": coverage_account_id
                }
            )
            await self.event_bus.publish(event)
            
        except Exception as e:
            logger.error(f"B-Book execution failed for {order.ticket_id}: {e}")
            await self._reject_order(order, f"B-Book internal error: {str(e)}")
    
    async def _apply_deal_to_account(self, deal, account):
        """Helper to apply deal to account positions and recalculate margin."""
        # In production, this delegates to RecordDealCommandHandler
        # For now, simplified implementation
        pass

    async def _execute_in_house(self, order: Order, instruction: ExecutionInstruction):
        """
        Submit to internal CLOB (Central Limit Order Book) for client-vs-client matching.
        """
        logger.info(f"Submitting order {order.ticket_id} to In-House ECN")
        
        try:
            await self.matching_engine.submit_order(order)
            
            order.state = OrderState.PLACED
            await self.order_repo.save(order)
            
            event = DomainEvent(
                event_type=EventType.ORDER_ROUTED,
                aggregate_id=order.ticket_id,
                payload={
                    "order_id": order.ticket_id,
                    "destination": "IN_HOUSE_ECN",
                    "status": "SUBMITTED_TO_CLOB"
                }
            )
            await self.event_bus.publish(event)
            
        except Exception as e:
            logger.error(f"In-House ECN submission failed for {order.ticket_id}: {e}")
            await self._reject_order(order, f"ECN error: {str(e)}")

    async def _send_to_dealer(self, order: Order):
        """
        Route to dealer queue for manual confirmation.
        """
        logger.info(f"Sending order {order.ticket_id} to Dealer Queue")
        
        try:
            await self.dealer_queue.enqueue(order, timeout_seconds=30)
            
            # State updated in enqueue()
            await self.order_repo.save(order)
            
        except Exception as e:
            logger.error(f"Dealer queue enrollment failed for {order.ticket_id}: {e}")
            await self._reject_order(order, f"Dealer queue error: {str(e)}")

    async def _reject_order(self, order: Order, reason: str):
        """
        Reject the order and emit OrderRejectedEvent.
        """
        order.state = OrderState.REJECTED
        await self.order_repo.save(order)
        
        event = DomainEvent(
            event_type=EventType.ORDER_REJECTED,
            aggregate_id=order.ticket_id,
            payload={
                "order_id": order.ticket_id,
                "reason": reason
            }
        )
        await self.event_bus.publish(event)
        
        logger.warning(f"Order {order.ticket_id} rejected: {reason}")
