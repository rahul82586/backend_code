"""
OMS Domain - Order Management System

This domain handles the Holy Trinity of trading:
- Order: Client's intent to trade
- Deal: Immutable execution record
- Position: Aggregate open state
"""
from dataclasses import dataclass, field
from datetime import datetime
from decimal import Decimal
from enum import Enum
from typing import Optional, List
import uuid

from core.domains.common.value_objects import Price, Volume, Money
from core.domains.instruments.models import Symbol


class OrderType(Enum):
    """Order types as per MT5."""
    BUY = "BUY"
    SELL = "SELL"
    BUY_LIMIT = "BUY_LIMIT"
    SELL_LIMIT = "SELL_LIMIT"
    BUY_STOP = "BUY_STOP"
    SELL_STOP = "SELL_STOP"
    BUY_STOP_LIMIT = "BUY_STOP_LIMIT"
    SELL_STOP_LIMIT = "SELL_STOP_LIMIT"


class OrderState(Enum):
    """Order lifecycle states."""
    NEW = "NEW"
    PLACED = "PLACED"
    PARTIALLY_FILLED = "PARTIALLY_FILLED"
    FILLED = "FILLED"
    CANCELLED = "CANCELLED"
    REJECTED = "REJECTED"
    EXPIRED = "EXPIRED"
    MODIFIED = "MODIFIED"


class DealType(Enum):
    """Deal types including corrections."""
    BUY = "BUY"
    SELL = "SELL"
    DEPOSIT = "DEPOSIT"
    WITHDRAWAL = "WITHDRAWAL"
    SWAP = "SWAP"
    COMMISSION = "COMMISSION"
    CORRECTION = "CORRECTION"  # MT5-style trade correction
    BONUS = "BONUS"
    FEE = "FEE"


@dataclass
class Order:
    """
    Order Entity - Represents Client Intent
    
    An order is the client's request to buy or sell a specific volume
    at a specific price (or market price). It is mutable until filled
    or cancelled.
    
    Attributes:
        ticket_id: Unique order identifier (MT5 style sequential)
        account_login: Client account login
        symbol: Trading instrument
        order_type: Type of order (Market, Limit, Stop, etc.)
        volume: Requested volume in lots
        price: Limit/Stop price (None for market orders)
        stop_loss: Stop Loss price level
        take_profit: Take Profit price level
        state: Current order state
        created_at: Order creation timestamp
        updated_at: Last modification timestamp
        filled_volume: Volume already executed
        average_fill_price: Weighted average fill price
    """
    ticket_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    account_login: str = ""
    symbol: str = ""
    order_type: OrderType = OrderType.BUY
    volume: Volume = field(default_factory=lambda: Volume(Decimal('0')))
    price: Optional[Price] = None
    stop_loss: Optional[Price] = None
    take_profit: Optional[Price] = None
    
    state: OrderState = OrderState.NEW
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime = field(default_factory=datetime.utcnow)
    
    filled_volume: Volume = field(default_factory=lambda: Volume(Decimal('0')))
    average_fill_price: Optional[Price] = None
    
    # Dealer assignment (for manual handling)
    dealer_id: Optional[str] = None
    dealer_comment: str = ""
    
    # External routing info
    external_order_id: Optional[str] = None
    liquidity_provider: Optional[str] = None
    
    # Magic number (client EA identifier)
    magic_number: int = 0
    
    # Comment from client
    comment: str = ""

    def can_be_modified(self) -> bool:
        """Check if order can be modified."""
        return self.state in [
            OrderState.NEW,
            OrderState.PLACED,
            OrderState.PARTIALLY_FILLED
        ]

    def can_be_cancelled(self) -> bool:
        """Check if order can be cancelled."""
        return self.state in [OrderState.NEW, OrderState.PLACED]

    def apply_fill(self, volume: Volume, price: Price) -> None:
        """
        Apply a fill to this order.
        
        Args:
            volume: Filled volume
            price: Fill price
            
        Raises:
            ValueError: If fill volume exceeds remaining order volume
        """
        remaining_volume = Volume(self.volume.value - self.filled_volume.value)
        
        if volume.value > remaining_volume.value:
            raise ValueError(
                f"Fill volume {volume.value} exceeds remaining "
                f"{remaining_volume.value}"
            )
        
        # Recalculate average fill price
        if self.average_fill_price is None:
            self.average_fill_price = price
        else:
            total_value = (
                self.average_fill_price.value * self.filled_volume.value +
                price.value * volume.value
            )
            new_total_volume = self.filled_volume.value + volume.value
            self.average_fill_price = Price(total_value / new_total_volume)
        
        # Update filled volume
        self.filled_volume = Volume(self.filled_volume.value + volume.value)
        self.updated_at = datetime.utcnow()
        
        # Update state
        if self.filled_volume.value >= self.volume.value:
            self.state = OrderState.FILLED
        else:
            self.state = OrderState.PARTIALLY_FILLED

    def get_remaining_volume(self) -> Volume:
        """Get remaining volume to be filled."""
        return Volume(self.volume.value - self.filled_volume.value)

    def is_active(self) -> bool:
        """Check if order is still active (not terminal state)."""
        return self.state not in [
            OrderState.FILLED,
            OrderState.CANCELLED,
            OrderState.REJECTED,
            OrderState.EXPIRED
        ]

    def to_dict(self) -> dict:
        """Convert to dictionary for serialization."""
        return {
            "ticket_id": self.ticket_id,
            "account_login": self.account_login,
            "symbol": self.symbol,
            "order_type": self.order_type.value,
            "volume": str(self.volume.value),
            "price": str(self.price.value) if self.price else None,
            "stop_loss": str(self.stop_loss.value) if self.stop_loss else None,
            "take_profit": str(self.take_profit.value) if self.take_profit else None,
            "state": self.state.value,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
            "filled_volume": str(self.filled_volume.value),
            "average_fill_price": str(self.average_fill_price.value) 
                if self.average_fill_price else None,
            "dealer_id": self.dealer_id,
            "external_order_id": self.external_order_id,
            "magic_number": self.magic_number,
            "comment": self.comment,
        }


@dataclass
class Deal:
    """
    Deal Entity - Immutable Execution Record
    
    A deal represents an actual execution that occurred. Unlike orders,
    deals are immutable facts - once created, they cannot be changed.
    Corrections are handled by creating opposing correction deals.
    
    This follows MT5's approach where every trade modification creates
    a chain of deals (original + reversal + correction).
    
    Attributes:
        deal_id: Unique deal identifier
        order_id: Reference to originating order
        account_login: Client account login
        symbol: Trading instrument
        deal_type: Type of deal (Buy, Sell, Correction, etc.)
        volume: Executed volume
        price: Execution price
        commission: Commission charged
        swap: Swap amount
        profit: Realized profit/loss
        created_at: Execution timestamp
        original_deal_id: For corrections, reference to original deal
        reason: Reason for deal (especially for corrections)
    """
    deal_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    order_id: str = ""
    account_login: str = ""
    symbol: str = ""
    deal_type: DealType = DealType.BUY
    volume: Volume = field(default_factory=lambda: Volume(Decimal('0')))
    price: Price = field(default_factory=lambda: Price(Decimal('0')))
    
    commission: Money = field(
        default_factory=lambda: Money(Decimal('0'), "USD")
    )
    swap: Money = field(
        default_factory=lambda: Money(Decimal('0'), "USD")
    )
    profit: Money = field(
        default_factory=lambda: Money(Decimal('0'), "USD")
    )
    
    created_at: datetime = field(default_factory=datetime.utcnow)
    
    # MT5 Correction Linkage
    original_deal_id: Optional[str] = None
    reason: Optional[str] = None
    
    # Dealer who executed/modified
    dealer_id: Optional[str] = None
    
    # External deal reference (from LP)
    external_deal_id: Optional[str] = None
    
    # Position ID this deal affects
    position_id: Optional[str] = None
    
    # Magic number and comment
    magic_number: int = 0
    comment: str = ""

    def __post_init__(self):
        """Validate deal after initialization."""
        # Deals should be immutable conceptually
        # In production, you might make fields read-only after creation
        pass

    def is_correction(self) -> bool:
        """Check if this deal is a correction."""
        return self.deal_type == DealType.CORRECTION

    def to_dict(self) -> dict:
        """Convert to dictionary for serialization."""
        return {
            "deal_id": self.deal_id,
            "order_id": self.order_id,
            "account_login": self.account_login,
            "symbol": self.symbol,
            "deal_type": self.deal_type.value,
            "volume": str(self.volume.value),
            "price": str(self.price.value),
            "commission": str(self.commission.amount),
            "commission_currency": self.commission.currency,
            "swap": str(self.swap.amount),
            "profit": str(self.profit.amount),
            "created_at": self.created_at.isoformat(),
            "original_deal_id": self.original_deal_id,
            "reason": self.reason,
            "dealer_id": self.dealer_id,
            "external_deal_id": self.external_deal_id,
            "position_id": self.position_id,
            "magic_number": self.magic_number,
            "comment": self.comment,
        }


@dataclass
class Position:
    """
    Position Entity - Aggregate Open State
    
    A position represents the current net open exposure for a specific
    symbol in an account. It is derived from the sequence of deals
    (Buys and Sells) and is updated with each new deal.
    
    Positions support:
    - Adding to existing positions (same direction)
    - Partial closes (opposite direction, smaller volume)
    - Full closes (opposite direction, equal volume)
    - Reversals (opposite direction, larger volume)
    
    Attributes:
        id: Unique position identifier ({account_login}:{symbol})
        account_login: Client account login
        symbol: Trading instrument
        volume: Current open volume
        side: Position direction (Buy or Sell)
        average_price: Weighted average entry price
        unrealized_pnl: Current floating P&L
        swap_accumulated: Total swap charges
        opened_at: Position opening timestamp
    """
    id: str = ""
    account_login: str = ""
    symbol: str = ""
    
    volume: Volume = field(default_factory=lambda: Volume(Decimal('0')))
    side: Optional[OrderType] = None  # BUY or SELL
    average_price: Optional[Price] = None
    
    unrealized_pnl: Money = field(
        default_factory=lambda: Money(Decimal('0'), "USD")
    )
    swap_accumulated: Money = field(
        default_factory=lambda: Money(Decimal('0'), "USD")
    )
    
    opened_at: datetime = field(default_factory=datetime.utcnow)
    last_updated: datetime = field(default_factory=datetime.utcnow)
    
    # External position reference (from LP)
    external_position_id: Optional[str] = None
    
    # Magic number and comment
    magic_number: int = 0
    comment: str = ""

    def apply_deal(self, deal: Deal) -> None:
        """
        Apply a deal to update position state.
        
        Logic:
        - Same direction as current position: Add to volume, recalc avg price
        - Opposite direction:
          - Smaller volume: Partial close
          - Equal volume: Full close
          - Larger volume: Reverse position
        
        Args:
            deal: The deal to apply
            
        Note:
            P&L realization is calculated but not applied to balance here.
            The Ledger service handles actual balance updates.
        """
        if deal.deal_type not in [DealType.BUY, DealType.SELL]:
            return  # Ignore non-trading deals
        
        deal_side = OrderType.BUY if deal.deal_type == DealType.BUY else OrderType.SELL
        
        # Initialize position if empty
        if self.volume.value == 0:
            self.volume = deal.volume
            self.side = deal_side
            self.average_price = deal.price
            self.opened_at = deal.created_at
            return
        
        if deal_side == self.side:
            # Adding to position - recalculate average price
            total_value = (
                self.average_price.value * self.volume.value +
                deal.price.value * deal.volume.value
            )
            new_volume = self.volume.value + deal.volume.value
            self.volume = Volume(new_volume)
            self.average_price = Price(total_value / new_volume)
        else:
            # Opposite direction - closing or reversing
            if deal.volume.value < self.volume.value:
                # Partial close
                self.volume = Volume(self.volume.value - deal.volume.value)
                # P&L realized but handled by Ledger
            elif deal.volume.value == self.volume.value:
                # Full close - position effectively closed
                self.volume = Volume(Decimal('0'))
                self.side = None
                self.average_price = None
                # Position should be archived by service
            else:
                # Reversal - close existing and open opposite
                new_volume = deal.volume.value - self.volume.value
                self.volume = Volume(new_volume)
                self.side = deal_side
                self.average_price = deal.price
                self.opened_at = deal.created_at
        
        self.last_updated = datetime.utcnow()

    def update_unrealized_pnl(self, current_market_price: Price) -> None:
        """
        Calculate current unrealized P&L based on market price.
        
        Args:
            current_market_price: Current market price for the symbol
        """
        if self.volume.value == 0 or self.average_price is None:
            self.unrealized_pnl = Money(Decimal('0'), "USD")
            return
        
        price_diff = current_market_price.value - self.average_price.value
        
        # For SELL positions, profit when price goes down
        if self.side == OrderType.SELL:
            price_diff = -price_diff
        
        # P&L = price_diff * volume * contract_size
        # Simplified here assuming contract_size = 1
        pnl_value = price_diff * self.volume.value
        self.unrealized_pnl = Money(pnl_value, "USD")

    def is_open(self) -> bool:
        """Check if position is still open."""
        return self.volume.value > 0

    def to_dict(self) -> dict:
        """Convert to dictionary for serialization."""
        return {
            "id": self.id,
            "account_login": self.account_login,
            "symbol": self.symbol,
            "volume": str(self.volume.value),
            "side": self.side.value if self.side else None,
            "average_price": str(self.average_price.value) 
                if self.average_price else None,
            "unrealized_pnl": str(self.unrealized_pnl.amount),
            "pnl_currency": self.unrealized_pnl.currency,
            "swap_accumulated": str(self.swap_accumulated.amount),
            "opened_at": self.opened_at.isoformat(),
            "last_updated": self.last_updated.isoformat(),
            "external_position_id": self.external_position_id,
            "magic_number": self.magic_number,
            "comment": self.comment,
        }
