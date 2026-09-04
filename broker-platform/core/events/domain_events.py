"""
Core Domain Events - The Glue That Prevents Rewrites

All domain events inherit from BaseEvent and are used to decouple
the core domain from infrastructure and intelligence layers.
"""
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Any, Dict, Optional
import uuid


class EventType(Enum):
    """Types of domain events."""
    # Order Events
    ORDER_CREATED = "order_created"
    ORDER_MODIFIED = "order_modified"
    ORDER_CANCELLED = "order_cancelled"
    ORDER_FILLED = "order_filled"
    ORDER_REJECTED = "order_rejected"
    
    # Deal Events
    DEAL_CREATED = "deal_created"
    DEAL_MODIFIED = "deal_modified"
    DEAL_REVERSED = "deal_reversed"
    
    # Position Events
    POSITION_OPENED = "position_opened"
    POSITION_CLOSED = "position_closed"
    POSITION_UPDATED = "position_updated"
    
    # Market Events
    TICK_RECEIVED = "tick_received"
    BOOK_UPDATED = "book_updated"
    BAR_AGGREGATED = "bar_aggregated"
    
    # Account Events
    ACCOUNT_CREATED = "account_created"
    ACCOUNT_UPDATED = "account_updated"
    BALANCE_CHANGED = "balance_changed"
    MARGIN_CALL = "margin_call"
    STOP_OUT = "stop_out"
    
    # System Events
    NODE_JOINED = "node_joined"
    NODE_LEFT = "node_left"
    CERTIFICATE_EXPIRING = "certificate_expiring"
    SYNC_REQUIRED = "sync_required"
    
    # Risk Events
    PRE_TRADE_CHECK_FAILED = "pre_trade_check_failed"
    POST_TRADE_CHECK_FAILED = "post_trade_check_failed"
    EXPOSURE_LIMIT_EXCEEDED = "exposure_limit_exceeded"


@dataclass
class BaseEvent:
    """Base class for all domain events."""
    event_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    timestamp: datetime = field(default_factory=datetime.utcnow)
    event_type: EventType = EventType.ORDER_CREATED
    aggregate_id: Optional[str] = None
    aggregate_type: Optional[str] = None
    metadata: Dict[str, Any] = field(default_factory=dict)
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert event to dictionary for serialization."""
        return {
            "event_id": self.event_id,
            "timestamp": self.timestamp.isoformat(),
            "event_type": self.event_type.value,
            "aggregate_id": self.aggregate_id,
            "aggregate_type": self.aggregate_type,
            "metadata": self.metadata,
        }


# ============= ORDER EVENTS =============

@dataclass
class OrderCreatedEvent(BaseEvent):
    """Event fired when a new order is created."""
    event_type: EventType = EventType.ORDER_CREATED
    account_id: Optional[str] = None
    symbol: Optional[str] = None
    order_type: Optional[str] = None  # MARKET, LIMIT, STOP, STOP_LIMIT
    side: Optional[str] = None  # BUY, SELL
    volume: Optional[float] = None
    price: Optional[float] = None
    stop_loss: Optional[float] = None
    take_profit: Optional[float] = None
    magic: Optional[int] = None
    comment: Optional[str] = None


@dataclass
class OrderModifiedEvent(BaseEvent):
    """Event fired when an order is modified."""
    event_type: EventType.ORDER_MODIFIED
    order_id: Optional[str] = None
    account_id: Optional[str] = None
    old_price: Optional[float] = None
    new_price: Optional[float] = None
    old_stop_loss: Optional[float] = None
    new_stop_loss: Optional[float] = None
    old_take_profit: Optional[float] = None
    new_take_profit: Optional[float] = None


@dataclass
class OrderCancelledEvent(BaseEvent):
    """Event fired when an order is cancelled."""
    event_type: EventType.ORDER_CANCELLED
    order_id: Optional[str] = None
    account_id: Optional[str] = None
    reason: Optional[str] = None


@dataclass
class OrderFilledEvent(BaseEvent):
    """Event fired when an order is filled."""
    event_type: EventType.ORDER_FILLED
    order_id: Optional[str] = None
    deal_id: Optional[str] = None
    account_id: Optional[str] = None
    symbol: Optional[str] = None
    side: Optional[str] = None
    volume: Optional[float] = None
    fill_price: Optional[float] = None
    commission: Optional[float] = None
    swap: Optional[float] = None
    profit: Optional[float] = None


@dataclass
class OrderRejectedEvent(BaseEvent):
    """Event fired when an order is rejected."""
    event_type: EventType.ORDER_REJECTED
    order_id: Optional[str] = None
    account_id: Optional[str] = None
    reason: Optional[str] = None
    error_code: Optional[int] = None


# ============= DEAL EVENTS =============

@dataclass
class DealCreatedEvent(BaseEvent):
    """Event fired when a new deal is created."""
    event_type: EventType.DEAL_CREATED
    deal_id: Optional[str] = None
    order_id: Optional[str] = None
    account_id: Optional[str] = None
    symbol: Optional[str] = None
    side: Optional[str] = None
    volume: Optional[float] = None
    price: Optional[float] = None
    commission: Optional[float] = None
    swap: Optional[float] = None
    profit: Optional[float] = None
    deal_type: Optional[str] = None  # DEAL_TYPE_BUY, DEAL_TYPE_SELL, etc.


@dataclass
class DealModifiedEvent(BaseEvent):
    """
    Event fired when a deal is modified (MT5 Trade Modification).
    
    This is critical for dealer corrections. Instead of editing the database,
    we create a modification event that triggers reversal and correction deals.
    """
    event_type: EventType.DEAL_MODIFIED
    deal_id: Optional[str] = None
    original_deal_id: Optional[str] = None
    account_id: Optional[str] = None
    modification_type: Optional[str] = None  # PRICE, TIME, VOLUME, etc.
    old_value: Optional[Any] = None
    new_value: Optional[Any] = None
    dealer_id: Optional[str] = None
    reason: Optional[str] = None
    audit_log: Optional[Dict[str, Any]] = None


@dataclass
class DealReversedEvent(BaseEvent):
    """Event fired when a deal is reversed (part of modification)."""
    event_type: EventType.DEAL_REVERSED
    reversal_deal_id: Optional[str] = None
    original_deal_id: Optional[str] = None
    account_id: Optional[str] = None
    reversal_reason: Optional[str] = None


# ============= POSITION EVENTS =============

@dataclass
class PositionOpenedEvent(BaseEvent):
    """Event fired when a new position is opened."""
    event_type: EventType.POSITION_OPENED
    position_id: Optional[str] = None
    account_id: Optional[str] = None
    symbol: Optional[str] = None
    side: Optional[str] = None
    volume: Optional[float] = None
    open_price: Optional[float] = None
    stop_loss: Optional[float] = None
    take_profit: Optional[float] = None


@dataclass
class PositionClosedEvent(BaseEvent):
    """Event fired when a position is closed."""
    event_type: EventType.POSITION_CLOSED
    position_id: Optional[str] = None
    account_id: Optional[str] = None
    symbol: Optional[str] = None
    volume: Optional[float] = None
    open_price: Optional[float] = None
    close_price: Optional[float] = None
    profit: Optional[float] = None
    commission: Optional[float] = None
    swap: Optional[float] = None


@dataclass
class PositionUpdatedEvent(BaseEvent):
    """Event fired when a position is updated (partial close, SL/TP change)."""
    event_type: EventType.POSITION_UPDATED
    position_id: Optional[str] = None
    account_id: Optional[str] = None
    old_volume: Optional[float] = None
    new_volume: Optional[float] = None
    old_stop_loss: Optional[float] = None
    new_stop_loss: Optional[float] = None
    old_take_profit: Optional[float] = None
    new_take_profit: Optional[float] = None


# ============= MARKET EVENTS =============

@dataclass
class TickReceivedEvent(BaseEvent):
    """Event fired when a new tick is received."""
    event_type: EventType.TICK_RECEIVED
    symbol: Optional[str] = None
    bid: Optional[float] = None
    ask: Optional[float] = None
    last: Optional[float] = None
    volume: Optional[float] = None
    timestamp_ns: Optional[int] = None  # Nanosecond precision


@dataclass
class BookUpdatedEvent(BaseEvent):
    """Event fired when the order book (DOM) is updated."""
    event_type: EventType.BOOK_UPDATED
    symbol: Optional[str] = None
    bids: Optional[list] = None  # List of (price, volume) tuples
    asks: Optional[list] = None  # List of (price, volume) tuples
    timestamp_ns: Optional[int] = None


@dataclass
class BarAggregatedEvent(BaseEvent):
    """Event fired when a bar is aggregated (for timeseries)."""
    event_type: EventType.BAR_AGGREGATED
    symbol: Optional[str] = None
    timeframe: Optional[str] = None  # 1m, 5m, 1h, etc.
    open: Optional[float] = None
    high: Optional[float] = None
    low: Optional[float] = None
    close: Optional[float] = None
    volume: Optional[float] = None
    bar_start: Optional[datetime] = None
    bar_end: Optional[datetime] = None


# ============= ACCOUNT EVENTS =============

@dataclass
class AccountCreatedEvent(BaseEvent):
    """Event fired when a new account is created."""
    event_type: EventType.ACCOUNT_CREATED
    account_id: Optional[str] = None
    login: Optional[int] = None
    group: Optional[str] = None
    account_type: Optional[str] = None  # real, demo, preliminary, contest, coverage
    currency: Optional[str] = None
    balance: Optional[float] = None
    leverage: Optional[int] = None


@dataclass
class AccountUpdatedEvent(BaseEvent):
    """Event fired when an account is updated."""
    event_type: EventType.ACCOUNT_UPDATED
    account_id: Optional[str] = None
    field_changed: Optional[str] = None
    old_value: Optional[Any] = None
    new_value: Optional[Any] = None


@dataclass
class BalanceChangedEvent(BaseEvent):
    """Event fired when an account balance changes."""
    event_type: EventType.BALANCE_CHANGED
    account_id: Optional[str] = None
    old_balance: Optional[float] = None
    new_balance: Optional[float] = None
    change_amount: Optional[float] = None
    change_reason: Optional[str] = None  # deposit, withdrawal, profit, etc.


@dataclass
class MarginCallEvent(BaseEvent):
    """Event fired when margin call level is reached."""
    event_type: EventType.MARGIN_CALL
    account_id: Optional[str] = None
    margin_level: Optional[float] = None
    threshold: Optional[float] = None
    equity: Optional[float] = None
    margin_required: Optional[float] = None


@dataclass
class StopOutEvent(BaseEvent):
    """Event fired when stop out level is reached and positions are closed."""
    event_type: EventType.STOP_OUT
    account_id: Optional[str] = None
    margin_level: Optional[float] = None
    threshold: Optional[float] = None
    positions_closed: Optional[list] = None


# ============= SYSTEM EVENTS =============

@dataclass
class NodeJoinedEvent(BaseEvent):
    """Event fired when a new node joins the cluster."""
    event_type: EventType.NODE_JOINED
    node_id: Optional[str] = None
    node_role: Optional[str] = None  # access, trade, history
    endpoint: Optional[str] = None
    certificate_expiry: Optional[datetime] = None


@dataclass
class NodeLeftEvent(BaseEvent):
    """Event fired when a node leaves the cluster."""
    event_type: EventType.NODE_LEFT
    node_id: Optional[str] = None
    reason: Optional[str] = None  # graceful, timeout, error


@dataclass
class CertificateExpiringEvent(BaseEvent):
    """Event fired when an SSL certificate is about to expire."""
    event_type: EventType.CERTIFICATE_EXPIRING
    node_id: Optional[str] = None
    certificate_type: Optional[str] = None
    expiry_date: Optional[datetime] = None
    days_remaining: Optional[int] = None


@dataclass
class SyncRequiredEvent(BaseEvent):
    """Event fired when cluster sync is required."""
    event_type: EventType.SYNC_REQUIRED
    source_node_id: Optional[str] = None
    target_node_id: Optional[str] = None
    sync_type: Optional[str] = None  # full, incremental
    checksum_mismatch: Optional[bool] = None


# ============= RISK EVENTS =============

@dataclass
class PreTradeCheckFailedEvent(BaseEvent):
    """Event fired when pre-trade risk check fails."""
    event_type: EventType.PRE_TRADE_CHECK_FAILED
    order_id: Optional[str] = None
    account_id: Optional[str] = None
    check_type: Optional[str] = None  # margin, exposure, symbol_allowed, etc.
    reason: Optional[str] = None
    details: Optional[Dict[str, Any]] = None


@dataclass
class PostTradeCheckFailedEvent(BaseEvent):
    """Event fired when post-trade risk check fails."""
    event_type: EventType.POST_TRADE_CHECK_FAILED
    deal_id: Optional[str] = None
    account_id: Optional[str] = None
    check_type: Optional[str] = None
    reason: Optional[str] = None
    details: Optional[Dict[str, Any]] = None


@dataclass
class ExposureLimitExceededEvent(BaseEvent):
    """Event fired when aggregate exposure limit is exceeded."""
    event_type: EventType.EXPOSURE_LIMIT_EXCEEDED
    symbol: Optional[str] = None
    current_exposure: Optional[float] = None
    limit: Optional[float] = None
    breach_type: Optional[str] = None  # net, gross, delta


# Event type mapping for deserialization
EVENT_TYPES = {
    EventType.ORDER_CREATED: OrderCreatedEvent,
    EventType.ORDER_MODIFIED: OrderModifiedEvent,
    EventType.ORDER_CANCELLED: OrderCancelledEvent,
    EventType.ORDER_FILLED: OrderFilledEvent,
    EventType.ORDER_REJECTED: OrderRejectedEvent,
    EventType.DEAL_CREATED: DealCreatedEvent,
    EventType.DEAL_MODIFIED: DealModifiedEvent,
    EventType.DEAL_REVERSED: DealReversedEvent,
    EventType.POSITION_OPENED: PositionOpenedEvent,
    EventType.POSITION_CLOSED: PositionClosedEvent,
    EventType.POSITION_UPDATED: PositionUpdatedEvent,
    EventType.TICK_RECEIVED: TickReceivedEvent,
    EventType.BOOK_UPDATED: BookUpdatedEvent,
    EventType.BAR_AGGREGATED: BarAggregatedEvent,
    EventType.ACCOUNT_CREATED: AccountCreatedEvent,
    EventType.ACCOUNT_UPDATED: AccountUpdatedEvent,
    EventType.BALANCE_CHANGED: BalanceChangedEvent,
    EventType.MARGIN_CALL: MarginCallEvent,
    EventType.STOP_OUT: StopOutEvent,
    EventType.NODE_JOINED: NodeJoinedEvent,
    EventType.NODE_LEFT: NodeLeftEvent,
    EventType.CERTIFICATE_EXPIRING: CertificateExpiringEvent,
    EventType.SYNC_REQUIRED: SyncRequiredEvent,
    EventType.PRE_TRADE_CHECK_FAILED: PreTradeCheckFailedEvent,
    EventType.POST_TRADE_CHECK_FAILED: PostTradeCheckFailedEvent,
    EventType.EXPOSURE_LIMIT_EXCEEDED: ExposureLimitExceededEvent,
}
