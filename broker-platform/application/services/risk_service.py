"""
Pre-Trade Risk Service for validating orders before execution.
Encapsulates all margin, permission, and account state checks.
"""
import logging
from decimal import Decimal
from typing import Optional

from core.domains.accounts.models import Account, Group
from core.domains.instruments.models import Symbol
from core.domains.oms.entities.order import Order, OrderType
from core.domains.common.value_objects import Money, Price, Volume
from core.events.domain_events import DomainEvent, OrderApproved, OrderRejected, EventType
from core.ports.interfaces import IEventBus

logger = logging.getLogger(__name__)


class PreTradeRiskService:
    """
    Service responsible for pre-trade validation.
    
    Architectural Purpose:
    Centralizes all risk checks required before an order can be accepted.
    This prevents code duplication across different order entry points 
    (API, FIX, Dealer Terminal) and ensures consistent enforcement of 
    Group rules and broker risk policies.
    """
    
    def __init__(self, event_bus: IEventBus):
        self.event_bus = event_bus

    async def validate_order(
        self, 
        order: Order, 
        account: Account, 
        symbol: Symbol, 
        current_price: Price
    ) -> bool:
        """
        Performs all pre-trade checks. Returns True if approved, False if rejected.
        Publishes OrderApproved or OrderRejected events accordingly.
        """
        logger.info(f"Running pre-trade checks for Order {order.ticket_id} on Account {account.login_id}")
        
        # 1. Account State Check
        if not account.can_trade():
            reason = "Account is disabled or pending KYC verification"
            logger.warning(f"Order {order.ticket_id} rejected: {reason}")
            await self._publish_rejection(order, reason)
            return False

        # 2. Symbol Permission Check (Group Rules)
        if not self._check_symbol_permission(account.group, symbol.name):
            reason = f"Symbol {symbol.name} is not allowed for Group {account.group.name}"
            logger.warning(f"Order {order.ticket_id} rejected: {reason}")
            await self._publish_rejection(order, reason)
            return False

        # 3. Trading Session Check
        # Note: In production, use a timezone-aware datetime
        from datetime import datetime
        current_time = datetime.utcnow().time()
        if not symbol.is_within_session(current_time):
            reason = f"Symbol {symbol.name} is currently outside trading sessions"
            logger.warning(f"Order {order.ticket_id} rejected: {reason}")
            await self._publish_rejection(order, reason)
            return False

        # 4. Volume Limits Check
        if not self._check_volume_limits(order.volume, symbol):
            reason = f"Volume {order.volume.value} exceeds limits for {symbol.name} (Min: {symbol.volume_min}, Max: {symbol.volume_max})"
            logger.warning(f"Order {order.ticket_id} rejected: {reason}")
            await self._publish_rejection(order, reason)
            return False

        # 5. Margin Check (Critical for Forex/CFD)
        if not await self._check_margin_requirement(order, account, symbol, current_price):
            reason = "Insufficient free margin to open this position"
            logger.warning(f"Order {order.ticket_id} rejected: {reason}")
            await self._publish_rejection(order, reason)
            return False

        # All checks passed
        logger.info(f"Order {order.ticket_id} approved by Pre-Trade Risk Service")
        await self._publish_approval(order)
        return True

    def _check_symbol_permission(self, group: Group, symbol_name: str) -> bool:
        """Checks if the group permissions allow trading this symbol."""
        # If permissions dict is empty, assume all allowed (open broker model)
        if not group.permissions:
            return True
        return group.permissions.get(symbol_name, False)

    def _check_volume_limits(self, volume: Volume, symbol: Symbol) -> bool:
        """Validates volume against symbol min/max and step."""
        if volume.value < symbol.volume_min or volume.value > symbol.volume_max:
            return False
        if not volume.is_valid_step(symbol.volume_step):
            return False
        return True

    async def _check_margin_requirement(
        self, 
        order: Order, 
        account: Account, 
        symbol: Symbol, 
        price: Price
    ) -> bool:
        """
        Calculates required margin and compares against Free Margin.
        Formula: (Volume * ContractSize * Price) / Leverage
        """
        margin_required = symbol.calculate_margin_required(order.volume.value, price.value)
        
        # Convert to Money object
        required_money = Money(margin_required, account.balance.currency)
        
        if required_money.amount > account.margin_free.amount:
            logger.debug(
                f"Margin check failed: Required {required_money.amount}, "
                f"Available {account.margin_free.amount}"
            )
            return False
        
        return True

    async def _publish_approval(self, order: Order) -> None:
        """Publishes OrderApprovedEvent."""
        event = OrderApproved(
            aggregate_id=order.ticket_id,
            payload={
                "ticket_id": order.ticket_id,
                "account_login": order.account_login,
                "symbol": order.symbol,
                "volume": str(order.volume.value),
                "approved_at": order.updated_at.isoformat()
            }
        )
        await self.event_bus.publish(event)

    async def _publish_rejection(self, order: Order, reason: str) -> None:
        """Publishes OrderRejectedEvent."""
        event = OrderRejected(
            aggregate_id=order.ticket_id,
            payload={
                "ticket_id": order.ticket_id,
                "account_login": order.account_login,
                "reason": reason,
                "rejected_at": order.updated_at.isoformat()
            }
        )
        await self.event_bus.publish(event)
