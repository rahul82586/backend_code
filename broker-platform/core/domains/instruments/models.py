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

    # Currency Fields
    base_currency: str = ""
    quote_currency: str = ""

    def __post_init__(self):
        if not self.base_currency or not self.quote_currency:
            base, quote = self.parse_currencies_from_name(self.name)
            if not self.base_currency:
                self.base_currency = base
            if not self.quote_currency:
                self.quote_currency = quote

    @staticmethod
    def parse_currencies_from_name(name: str) -> tuple[str, str]:
        """
        Parses base and quote currency from symbol name.
        e.g., 'EURUSD' -> ('EUR', 'USD'), 'USDJPY' -> ('USD', 'JPY'), 'EURJPY' -> ('EUR', 'JPY').
        Raises ValueError if quote currency cannot be determined.
        """
        clean_name = name.upper().replace("/", "").replace("_", "").strip()

        known_bases = {"XAU", "XAG", "WTI", "BRN", "BTC", "ETH", "SOL", "USDT", "USDC"}
        for base in known_bases:
            if clean_name.startswith(base):
                quote = clean_name[len(base):]
                if not quote:
                    quote = "USD"
                return base, quote

        if len(clean_name) >= 6:
            return clean_name[:3], clean_name[3:6]

        raise ValueError(f"Cannot determine base and quote currency for symbol '{name}'")

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
