from dataclasses import dataclass, field
from datetime import datetime
from decimal import Decimal
from enum import Enum
from typing import Optional

from core.domains.common.value_objects import Price, Volume

class OrderType(Enum):
    BUY = "BUY"
    SELL = "SELL"
    BUY_LIMIT = "BUY_LIMIT"
    SELL_LIMIT = "SELL_LIMIT"
    BUY_STOP = "BUY_STOP"
    SELL_STOP = "SELL_STOP"

class OrderState(Enum):
    NEW = "NEW"
    PLACED = "PLACED"
    PARTIALLY_FILLED = "PARTIALLY_FILLED"
    FILLED = "FILLED"
    CANCELLED = "CANCELLED"
    REJECTED = "REJECTED"
    EXPIRED = "EXPIRED"

@dataclass
class Order:
    """
    Represents Client Intent.
    Mutable until filled or cancelled.
    
    Architectural Purpose:
    Captures the trader's order request. State transitions are enforced
    via business methods to prevent invalid state changes.
    """
    ticket_id: str
    account_login: str
    symbol: str
    order_type: OrderType
    volume: Volume
    price: Optional[Price] = None  # Null for Market Orders
    stop_loss: Optional[Price] = None
    take_profit: Optional[Price] = None
    
    state: OrderState = OrderState.NEW
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime = field(default_factory=datetime.utcnow)
    
    filled_volume: Volume = field(default_factory=lambda: Volume(Decimal('0')))
    average_fill_price: Optional[Price] = None

    def can_be_modified(self) -> bool:
        """Returns True if order is in a state that allows modification."""
        return self.state in [OrderState.NEW, OrderState.PLACED, OrderState.PARTIALLY_FILLED]

    def can_be_cancelled(self) -> bool:
        """Returns True if order is in a state that allows cancellation."""
        return self.state in [OrderState.NEW, OrderState.PLACED]

    def apply_fill(self, volume: Volume, price: Price):
        """
        Updates order state based on a fill.
        Recalculates average fill price using proper weighted average.
        """
        if self.filled_volume.value + volume.value > self.volume.value:
            raise ValueError("Fill volume exceeds order volume")
        
        # Recalculate average price
        current_val = (self.average_fill_price.value * self.filled_volume.value 
                      if self.average_fill_price else Decimal('0'))
        new_fill_val = price.value * volume.value
        new_vol = self.filled_volume.value + volume.value
        
        self.average_fill_price = Price((current_val + new_fill_val) / new_vol)
        self.filled_volume = Volume(new_vol)
        self.updated_at = datetime.utcnow()

        if self.filled_volume.value == self.volume.value:
            self.state = OrderState.FILLED
        else:
            self.state = OrderState.PARTIALLY_FILLED

    def reject(self):
        """Transitions order to REJECTED state."""
        self.state = OrderState.REJECTED
        self.updated_at = datetime.utcnow()

    def cancel(self):
        """Transitions order to CANCELLED state."""
        if not self.can_be_cancelled():
            raise ValueError(f"Cannot cancel order in state {self.state}")
        self.state = OrderState.CANCELLED
        self.updated_at = datetime.utcnow()
