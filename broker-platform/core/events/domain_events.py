"""
Domain Events - The Nervous System of the Platform

These immutable events are the only way different bounded contexts communicate,
preventing tight coupling and enabling independent evolution of services.
"""
import uuid
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any, Optional
from enum import Enum


class EventType(Enum):
    """Enumeration of all possible domain events."""
    # OMS Events
    ORDER_CREATED = "order.created"
    ORDER_MODIFIED = "order.modified"
    ORDER_CANCELLED = "order.cancelled"
    ORDER_REJECTED = "order.rejected"
    ORDER_APPROVED = "order.approved"  # Added for Phase 4
    
    DEAL_CREATED = "deal.created"
    DEAL_MODIFIED = "deal.modified"  # For MT5-style trade corrections
    
    POSITION_OPENED = "position.opened"
    POSITION_CLOSED = "position.closed"
    POSITION_UPDATED = "position.updated"

    # Market Data Events
    TICK_RECEIVED = "market.tick_received"
    BOOK_UPDATED = "market.book_updated"
    BAR_AGGREGATED = "market.bar_aggregated"

    # System/Risk Events
    MARGIN_CALL = "risk.margin_call"
    STOP_OUT = "risk.stop_out"
    NODE_HEARTBEAT = "system.node_heartbeat"


@dataclass(frozen=True)
class DomainEvent:
    """
    Base class for all domain events.
    
    Architectural Purpose:
    Acts as the standard envelope for communication between bounded contexts.
    Being frozen ensures immutability once created, guaranteeing event integrity
    as it travels through the Event Bus.
    """
    event_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    timestamp: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    aggregate_id: Optional[str] = None  # The ID of the main entity (e.g., OrderID, AccountID)
    payload: dict[str, Any] = field(default_factory=dict)
    event_type: EventType = EventType.ORDER_CREATED

    def to_dict(self) -> dict[str, Any]:
        """Serialize event for transport (e.g., JSON for Redis)."""
        return {
            "event_id": self.event_id,
            "timestamp": self.timestamp.isoformat(),
            "aggregate_id": self.aggregate_id,
            "event_type": self.event_type.value,
            "payload": self.payload
        }


# =============================================================================
# OMS (Order Management System) Events
# =============================================================================

@dataclass(frozen=True)
class OrderCreated(DomainEvent):
    """Published when a new order is created and accepted by the system."""
    event_type: EventType = field(default=EventType.ORDER_CREATED, init=False)
    # Payload expects: symbol, side, quantity, price, order_type, account_id


@dataclass(frozen=True)
class OrderModified(DomainEvent):
    """Published when an existing order is modified (price/quantity)."""
    event_type: EventType = field(default=EventType.ORDER_MODIFIED, init=False)
    # Payload expects: order_id, new_price, new_quantity, reason


@dataclass(frozen=True)
class OrderCancelled(DomainEvent):
    """Published when an order is cancelled."""
    event_type: EventType = field(default=EventType.ORDER_CANCELLED, init=False)
    # Payload expects: order_id, reason


@dataclass(frozen=True)
class OrderRejected(DomainEvent):
    """Published when an order is rejected (e.g., risk check failure)."""
    event_type: EventType = field(default=EventType.ORDER_REJECTED, init=False)
    # Payload expects: order_id, reason_code, message


@dataclass(frozen=True)
class OrderApproved(DomainEvent):
    """Published when an order passes all pre-trade risk checks."""
    event_type: EventType = field(default=EventType.ORDER_APPROVED, init=False)
    # Payload expects: order_id, account_login, symbol, volume, approved_at


@dataclass(frozen=True)
class DealCreated(DomainEvent):
    """Published when a new deal (trade) is executed."""
    event_type: EventType = field(default=EventType.DEAL_CREATED, init=False)
    # Payload expects: deal_id, order_id, price, quantity, commission, swap


@dataclass(frozen=True)
class DealModified(DomainEvent):
    """
    Specific to MT5-style trade corrections.
    Used when a dealer manually corrects a past deal.
    """
    event_type: EventType = field(default=EventType.DEAL_MODIFIED, init=False)
    # Payload expects: original_deal_id, correction_deal_id, reason, actor_id


@dataclass(frozen=True)
class PositionUpdated(DomainEvent):
    """Published when a position's P&L or margin changes."""
    event_type: EventType = field(default=EventType.POSITION_UPDATED, init=False)
    # Payload expects: position_id, current_price, unrealized_pnl, margin_used


# =============================================================================
# Market Data Events
# =============================================================================

@dataclass(frozen=True)
class TickReceived(DomainEvent):
    """Published when a new tick is received from a liquidity provider."""
    event_type: EventType = field(default=EventType.TICK_RECEIVED, init=False)
    # Payload expects: symbol, bid, ask, last_volume, exchange_timestamp


@dataclass(frozen=True)
class BookUpdated(DomainEvent):
    """Published when the order book (DOM) is updated."""
    event_type: EventType = field(default=EventType.BOOK_UPDATED, init=False)
    # Payload expects: symbol, bids_list, asks_list, sequence_number


# =============================================================================
# Risk Events
# =============================================================================

@dataclass(frozen=True)
class MarginCallEvent(DomainEvent):
    """Published when an account hits margin call level."""
    event_type: EventType = field(default=EventType.MARGIN_CALL, init=False)
    # Payload expects: account_id, margin_level, required_margin


@dataclass(frozen=True)
class StopOutEvent(DomainEvent):
    """Published when positions are forcibly closed due to insufficient margin."""
    event_type: EventType = field(default=EventType.STOP_OUT, init=False)
    # Payload expects: account_id, position_id, close_price, reason
