from dataclasses import dataclass
from decimal import Decimal, InvalidOperation
from typing import Union

@dataclass(frozen=True)
class Money:
    """
    Value Object for Currency.
    Ensures no floating point math occurs on balances.
    """
    amount: Decimal
    currency: str = "USD"

    def __post_init__(self):
        if not isinstance(self.amount, Decimal):
            object.__setattr__(self, 'amount', Decimal(str(self.amount)))
        if self.amount < 0:
            raise ValueError("Money amount cannot be negative")

    def __add__(self, other: 'Money') -> 'Money':
        if self.currency != other.currency:
            raise ValueError("Cannot add money with different currencies")
        return Money(self.amount + other.amount, self.currency)

    def __sub__(self, other: 'Money') -> 'Money':
        if self.currency != other.currency:
            raise ValueError("Cannot subtract money with different currencies")
        return Money(self.amount - other.amount, self.currency)

@dataclass(frozen=True)
class Price:
    """
    Value Object for Asset Price.
    Handles tick precision implicitly via string conversion.
    """
    value: Decimal

    def __post_init__(self):
        if not isinstance(self.value, Decimal):
            object.__setattr__(self, 'value', Decimal(str(self.value)))
        if self.value <= 0:
            raise ValueError("Price must be positive")

@dataclass(frozen=True)
class Volume:
    """
    Value Object for Trade Volume (Lots).
    Enforces minimum lot steps (e.g., 0.01).
    """
    value: Decimal

    def __post_init__(self):
        if not isinstance(self.value, Decimal):
            object.__setattr__(self, 'value', Decimal(str(self.value)))
        if self.value <= 0:
            raise ValueError("Volume must be positive")

    def is_valid_step(self, step: Decimal) -> bool:
        """Checks if volume aligns with symbol step (e.g., 0.01)"""
        remainder = self.value % step
        # Allow for minor decimal precision issues
        return remainder == 0 or abs(remainder - step) < Decimal('1E-8')
