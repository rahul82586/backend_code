"""
Domain models for the broker platform.

All models are immutable dataclasses with no I/O dependencies.
Prices and quantities use fixed-point arithmetic (integers) to avoid floating-point errors.
"""

from dataclasses import dataclass, field
from datetime import datetime
from decimal import Decimal
from enum import Enum, auto
from typing import Optional, List
from uuid import UUID, uuid4


# =============================================================================
# ENUMS
# =============================================================================

class OrderSide(Enum):
    BUY = "BUY"
    SELL = "SELL"


class OrderType(Enum):
    MARKET = "MARKET"
    LIMIT = "LIMIT"
    STOP = "STOP"
    STOP_LIMIT = "STOP_LIMIT"


class OrderTimeInForce(Enum):
    GTC = "GTC"  # Good Till Cancelled
    IOC = "IOC"  # Immediate Or Cancel
    FOK = "FOK"  # Fill Or Kill
    DAY = "DAY"  # Day order
    GTD = "GTD"  # Good Till Date


class OrderStatus(Enum):
    NEW = "NEW"
    PENDING_NEW = "PENDING_NEW"
    PARTIALLY_FILLED = "PARTIALLY_FILLED"
    FILLED = "FILLED"
    CANCELLED = "CANCELLED"
    REJECTED = "REJECTED"
    PENDING_CANCEL = "PENDING_CANCEL"
    PENDING_REPLACE = "PENDING_REPLACE"
    PENDING_DEALER = "PENDING_DEALER"  # Awaiting dealer approval (A-Book)


class OrderBook(Enum):
    """A-Book (external hedge) vs B-Book (internal risk)."""
    A_BOOK = "A_BOOK"
    B_BOOK = "B_BOOK"


class AccountMode(Enum):
    HEDGE = "HEDGE"      # Multiple positions per symbol
    NETTING = "NETTING"  # Single position per symbol


class PositionSide(Enum):
    BUY = "BUY"
    SELL = "SELL"


class DealType(Enum):
    BUY = "BUY"
    SELL = "SELL"
    BALANCE = "BALANCE"          # Deposit/withdrawal
    CREDIT = "CREDIT"
    CHARGE = "CHARGE"            # Commission/fee
    SWAP = "SWAP"                # Swap rollover
    BONUS = "BONUS"


# =============================================================================
# VALUE OBJECTS (Fixed-Point Arithmetic)
# =============================================================================

@dataclass(frozen=True)
class Price:
    """
    Fixed-point price representation.
    
    Stores price as integer * 10^(-digits) to avoid floating-point errors.
    Example: EURUSD at 1.08543 with digits=5 → raw_value=108543
    """
    raw_value: int
    digits: int
    
    @classmethod
    def from_decimal(cls, value: Decimal, digits: int) -> 'Price':
        multiplier = 10 ** digits
        raw = int(value * multiplier)
        return cls(raw_value=raw, digits=digits)
    
    @classmethod
    def from_float(cls, value: float, digits: int) -> 'Price':
        return cls.from_decimal(Decimal(str(value)), digits)
    
    def to_decimal(self) -> Decimal:
        return Decimal(self.raw_value) / (10 ** self.digits)
    
    def __str__(self) -> str:
        return f"{self.to_decimal():.{self.digits}f}"


@dataclass(frozen=True)
class Quantity:
    """
    Fixed-point quantity representation (lots).
    
    Stored as integer * 10000 to support 4 decimal places (e.g., 0.0001 lots).
    Example: 1.5 lots → raw_value=15000
    """
    raw_value: int
    
    LOT_MULTIPLIER = 10000
    
    @classmethod
    def from_lots(cls, lots: float) -> 'Quantity':
        raw = int(lots * cls.LOT_MULTIPLIER)
        return cls(raw_value=raw)
    
    def to_lots(self) -> float:
        return self.raw_value / self.LOT_MULTIPLIER
    
    def __str__(self) -> str:
        return f"{self.to_lots():.4f}"


@dataclass(frozen=True)
class Money:
    """
    Fixed-point monetary value.
    
    Stored in cents/smallest currency unit to avoid floating-point errors.
    Example: $123.45 → raw_value=12345
    """
    raw_value: int
    currency: str
    
    @classmethod
    def from_decimal(cls, value: Decimal, currency: str) -> 'Money':
        multiplier = 100  # cents
        raw = int(value * multiplier)
        return cls(raw_value=raw, currency=currency)
    
    def to_decimal(self) -> Decimal:
        return Decimal(self.raw_value) / 100
    
    def __str__(self) -> str:
        return f"{self.to_decimal():.2f} {self.currency}"
    
    def __add__(self, other: 'Money') -> 'Money':
        if self.currency != other.currency:
            raise ValueError(f"Cannot add different currencies: {self.currency} vs {other.currency}")
        return Money(raw_value=self.raw_value + other.raw_value, currency=self.currency)
    
    def __sub__(self, other: 'Money') -> 'Money':
        if self.currency != other.currency:
            raise ValueError(f"Cannot subtract different currencies: {self.currency} vs {other.currency}")
        return Money(raw_value=self.raw_value - other.raw_value, currency=self.currency)


# =============================================================================
# DOMAIN MODELS
# =============================================================================

@dataclass(frozen=True)
class Order:
    """Immutable order representation."""
    
    order_id: UUID
    client_order_id: str
    account_id: str
    symbol: str
    
    side: OrderSide
    type: OrderType
    time_in_force: OrderTimeInForce
    
    quantity: Quantity
    filled_quantity: Quantity = field(default_factory=lambda: Quantity(raw_value=0))
    
    limit_price: Optional[Price] = None
    stop_price: Optional[Price] = None
    take_profit_ticks: Optional[int] = None
    stop_loss_ticks: Optional[int] = None
    
    status: OrderStatus = OrderStatus.NEW
    book: OrderBook = OrderBook.B_BOOK  # Default to B-Book
    
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime = field(default_factory=datetime.utcnow)
    expires_at: Optional[datetime] = None
    
    reject_reason: Optional[str] = None
    dealer_notes: Optional[str] = None
    
    # Risk metadata
    margin_required: Optional[Money] = None
    slippage_tolerance_ticks: Optional[int] = None
    
    @classmethod
    def create(
        cls,
        account_id: str,
        symbol: str,
        side: OrderSide,
        order_type: OrderType,
        quantity: Quantity,
        time_in_force: OrderTimeInForce = OrderTimeInForce.GTC,
        limit_price: Optional[Price] = None,
        stop_price: Optional[Price] = None,
        client_order_id: Optional[str] = None,
        **kwargs
    ) -> 'Order':
        """Factory method to create a new order with generated IDs."""
        return cls(
            order_id=uuid4(),
            client_order_id=client_order_id or str(uuid4()),
            account_id=account_id,
            symbol=symbol,
            side=side,
            type=order_type,
            time_in_force=time_in_force,
            quantity=quantity,
            limit_price=limit_price,
            stop_price=stop_price,
            **kwargs
        )
    
    def with_status(self, status: OrderStatus, reason: Optional[str] = None) -> 'Order':
        """Return a new order with updated status."""
        return Order(
            **{f.name: getattr(self, f.name) for f in self.__dataclass_fields__},
            status=status,
            reject_reason=reason,
            updated_at=datetime.utcnow()
        )
    
    def with_fill(self, fill_quantity: Quantity) -> 'Order':
        """Return a new order with updated filled quantity."""
        new_filled = Quantity(raw_value=self.filled_quantity.raw_value + fill_quantity.raw_value)
        new_status = OrderStatus.FILLED if new_filled.raw_value >= self.quantity.raw_value else OrderStatus.PARTIALLY_FILLED
        return self.with_status(new_status)
    
    @property
    def remaining_quantity(self) -> Quantity:
        return Quantity(raw_value=self.quantity.raw_value - self.filled_quantity.raw_value)
    
    @property
    def is_complete(self) -> bool:
        return self.status in (OrderStatus.FILLED, OrderStatus.CANCELLED, OrderStatus.REJECTED)


@dataclass(frozen=True)
class Position:
    """Immutable position representation."""
    
    position_id: UUID
    account_id: str
    symbol: str
    side: PositionSide
    volume: Quantity
    
    open_price: Price
    current_price: Price
    
    unrealized_pnl: Money = field(default_factory=lambda: Money(raw_value=0, currency="USD"))
    
    take_profit_ticks: Optional[int] = None
    stop_loss_ticks: Optional[int] = None
    
    opened_at: datetime = field(default_factory=datetime.utcnow)
    order_id: Optional[UUID] = None
    
    # Swap/rollover
    swap_long: Money = field(default_factory=lambda: Money(raw_value=0, currency="USD"))
    swap_short: Money = field(default_factory=lambda: Money(raw_value=0, currency="USD"))
    accumulated_swap: Money = field(default_factory=lambda: Money(raw_value=0, currency="USD"))
    
    @property
    def equity(self) -> Money:
        """Calculate position equity (unrealized P&L + accumulated swap)."""
        return self.unrealized_pnl + self.accumulated_swap


@dataclass(frozen=True)
class Deal:
    """Immutable deal (transaction) representation."""
    
    deal_id: UUID
    account_id: str
    order_id: UUID
    position_id: Optional[UUID]
    symbol: str
    
    type: DealType
    volume: Quantity
    price: Price
    
    commission: Money
    swap: Money
    profit: Money
    
    comment: str = ""
    timestamp: datetime = field(default_factory=datetime.utcnow)


@dataclass(frozen=True)
class AccountBalance:
    """Immutable account balance snapshot."""
    
    account_id: str
    balance: Money
    equity: Money
    margin_used: Money
    margin_free: Money
    margin_level_bps: int  # Basis points (e.g., 50000 = 500%)
    
    unrealized_pnl: Money
    realized_pnl: Money
    
    currency: str
    updated_at: datetime = field(default_factory=datetime.utcnow)
    
    @property
    def margin_level_percent(self) -> float:
        return self.margin_level_bps / 100.0


@dataclass(frozen=True)
class FillEvent:
    """Event representing an order fill."""
    
    event_id: UUID
    order_id: UUID
    account_id: str
    symbol: str
    
    fill_price: Price
    fill_quantity: Quantity
    commission: Money
    
    timestamp: datetime = field(default_factory=datetime.utcnow)
    liquidity_provider: Optional[str] = None  # For A-Book fills
    
    @property
    def fill_value(self) -> Money:
        """Calculate total fill value (price * quantity)."""
        # Simplified calculation; real implementation needs contract size
        price_decimal = self.fill_price.to_decimal()
        lots = self.fill_quantity.to_lots()
        value = price_decimal * lots * 100000  # FX standard lot size
        return Money.from_decimal(value, self.commission.currency)
