from dataclasses import dataclass, field
from datetime import time
from typing import List, Optional
from decimal import Decimal

@dataclass
class TradingSession:
    start: time
    end: time
    day_of_week: int = 0  # 0=Monday, 6=Sunday

@dataclass
class Symbol:
    """
    Represents a tradable instrument (e.g., EURUSD, XAUUSD).
    Mirrors MT5 Symbol properties.
    """
    name: str
    path: str  # e.g., "Forex\EURUSD"
    
    # Pricing
    tick_size: Decimal
    tick_value: Decimal
    contract_size: Decimal
    digits: int
    
    # Limits
    volume_min: Decimal
    volume_max: Decimal
    volume_step: Decimal
    
    # Margins
    margin_initial_percent: Decimal  # e.g., 3.33% for 1:30 leverage
    margin_maintenance_percent: Decimal
    
    # Sessions
    sessions: List[TradingSession] = field(default_factory=list)
    
    # Trading Mode
    is_trade_allowed: bool = True
    fill_mode: str = "FOK"  # FOK, IOC, Return

    def is_within_session(self, current_time: time) -> bool:
        # Simplified session check logic
        # In production, handle overnight sessions spanning midnight
        return any(s.start <= current_time <= s.end for s in self.sessions)

    def calculate_margin_required(self, volume: Decimal, price: Decimal) -> Decimal:
        """
        Calculates initial margin required to open a position.
        Formula: (Volume * ContractSize * Price) / Leverage
        """
        gross_value = volume * self.contract_size * price
        return gross_value * (self.margin_initial_percent / Decimal('100'))
