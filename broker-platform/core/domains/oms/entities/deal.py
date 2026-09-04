from dataclasses import dataclass, field
from datetime import datetime
from decimal import Decimal
from enum import Enum
from typing import Optional

from core.domains.common.value_objects import Price, Volume, Money

class DealType(Enum):
    BUY = "BUY"
    SELL = "SELL"
    DEPOSIT = "DEPOSIT"
    WITHDRAWAL = "WITHDRAWAL"
    SWAP = "SWAP"
    COMMISSION = "COMMISSION"
    CORRECTION = "CORRECTION"  # MT5 Style Correction

@dataclass
class Deal:
    """
    Immutable Execution Record.
    Once created, this fact cannot change.
    Corrections require a new opposing Deal.
    
    Architectural Purpose:
    Represents the atomic truth of what happened in the market.
    Used for ledger updates, audit trails, and position construction.
    """
    deal_id: str
    order_id: str
    account_login: str
    symbol: str
    deal_type: DealType
    volume: Volume
    price: Price
    
    commission: Money
    swap: Money
    profit: Money = field(default_factory=lambda: Money(Decimal('0'), "USD"))
    
    created_at: datetime = field(default_factory=datetime.utcnow)
    
    # MT5 Correction Linkage
    # If this is a correction deal, links to the original deal being corrected
    original_deal_id: Optional[str] = None 
    reason: Optional[str] = None

    def __post_init__(self):
        """
        Enforce immutability conceptually.
        In production DB, this row would be append-only.
        """
        pass

    def create_correction(self, correction_deal_id: str, reason: str) -> 'Deal':
        """
        Creates a new Deal that corrects this one.
        The correction deal has opposite values to neutralize the original.
        """
        return Deal(
            deal_id=correction_deal_id,
            order_id=self.order_id,
            account_login=self.account_login,
            symbol=self.symbol,
            deal_type=DealType.CORRECTION,
            volume=self.volume,
            price=self.price,
            commission=Money(-self.commission.amount, self.commission.currency),
            swap=Money(-self.swap.amount, self.swap.currency),
            profit=Money(-self.profit.amount, self.profit.currency),
            original_deal_id=self.deal_id,
            reason=reason,
            created_at=datetime.utcnow()
        )
