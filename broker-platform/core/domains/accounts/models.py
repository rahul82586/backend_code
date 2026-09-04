"""
Accounts Domain - The MT5 Core

This domain handles Groups (as rule engines) and Accounts (Real, Demo, 
Preliminary, Coverage, Contest, Manager, Dealer).

The Group entity is the brain that dictates:
- Margin & Leverage rules
- Commissions & Swaps
- Permissions (allowed symbols, max positions, etc.)
- Routing rules (A-Book vs B-Book)
"""
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Optional
import uuid


class AccountType(Enum):
    """Account types as per MT5."""
    REAL = "real"
    DEMO = "demo"
    PRELIMINARY = "preliminary"  # KYC pending
    CONTEST = "contest"
    COVERAGE = "coverage"  # Internal hedge account
    MANAGER = "manager"
    DEALER = "dealer"


class GroupPermission(Enum):
    """Group permissions."""
    ALLOW_HEDGING = "allow_hedging"
    ALLOW_SHORT_SELLING = "allow_short_selling"
    ALLOW_PENDING_ORDERS = "allow_pending_orders"
    ALLOW_DEPOSIT = "deposit_allowed"
    ALLOW_WITHDRAWAL = "withdraw_allowed"
    ALLOW_TRADE = "trade_allowed"
    VIEW_ONLY = "view_only"
    INTERNAL_ONLY = "internal_only"


@dataclass
class CommissionRule:
    """Commission rule for a group."""
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    type: str = "per_lot"  # per_lot, per_deal, percent
    symbol_group: str = "*"  # Symbol pattern (e.g., "FOREX:*")
    value: float = 0.0
    currency: str = "USD"
    percent: float = 0.0  # For percent-based commissions
    min_value: float = 0.0
    max_value: Optional[float] = None


@dataclass
class SwapConfiguration:
    """Swap configuration for a group."""
    calculation_mode: str = "points"  # points, percent, disabled
    rollover_time: str = "22:00"
    triple_swap_day: str = "Wednesday"  # Day for triple swap


@dataclass
class RoutingRule:
    """Routing rule for order execution."""
    default_mode: str = "b_book"  # a_book, b_book, in_house_ecn, internal_hedge, simulation, none
    a_book_threshold_lots: Optional[float] = None
    lp_priority: List[str] = field(default_factory=list)  # Priority list of LPs


@dataclass
class GroupPermissions:
    """Permissions for a group."""
    allowed_symbols: List[str] = field(default_factory=lambda: ["*"])
    max_positions: int = 200
    max_orders: int = 100
    allow_hedging: bool = True
    allow_short_selling: bool = True
    allow_pending_orders: bool = True
    deposit_allowed: bool = True
    withdraw_allowed: bool = True
    trade_allowed: bool = True
    view_only: bool = False
    internal_only: bool = False
    negative_balance_protection: bool = True


@dataclass
class Group:
    """
    Group Entity - The Rule Engine
    
    In MT5, a Group is not just a label; it's a comprehensive rule engine
    that controls all aspects of accounts assigned to it.
    """
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    name: str = ""
    type: str = "real"  # real, demo, preliminary, contest, coverage
    currency: str = "USD"
    
    # Margin & Leverage
    leverage_default: int = 100
    leverage_max: int = 500
    margin_call_level: float = 0.8
    stop_out_level: float = 0.5
    
    # Rules
    permissions: GroupPermissions = field(default_factory=GroupPermissions)
    commissions: List[CommissionRule] = field(default_factory=list)
    swaps: SwapConfiguration = field(default_factory=SwapConfiguration)
    routing: RoutingRule = field(default_factory=RoutingRule)
    
    # Contest-specific (if applicable)
    contest_duration_days: Optional[int] = None
    virtual_balance: Optional[float] = None
    
    # Metadata
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime = field(default_factory=datetime.utcnow)
    is_active: bool = True
    
    def is_symbol_allowed(self, symbol: str) -> bool:
        """Check if a symbol is allowed for this group."""
        allowed = self.permissions.allowed_symbols
        if "*" in allowed:
            return True
        
        for pattern in allowed:
            if pattern.endswith("*"):
                prefix = pattern[:-1]
                if symbol.startswith(prefix):
                    return True
            elif symbol == pattern:
                return True
        
        return False
    
    def calculate_margin(self, symbol_config: Dict, volume: float, 
                         price: float) -> float:
        """Calculate required margin for a trade."""
        contract_size = symbol_config.get("contract_size", 100000)
        margin_percent = symbol_config.get("margins", {}).get(
            "initial_percent", 1.0
        )
        
        # Apply group leverage
        effective_leverage = min(self.leverage_default, self.leverage_max)
        leverage_factor = 1.0 / effective_leverage
        
        notional = volume * contract_size * price
        margin = notional * (margin_percent / 100.0) * leverage_factor
        
        return margin
    
    def calculate_commission(self, symbol: str, volume: float, 
                             deal_value: float) -> float:
        """Calculate commission for a deal."""
        for rule in self.commissions:
            # Check if symbol matches pattern
            if rule.symbol_group.endswith("*"):
                prefix = rule.symbol_group[:-1]
                if not symbol.startswith(prefix):
                    continue
            elif rule.symbol_group != "*":
                if symbol != rule.symbol_group:
                    continue
            
            # Calculate based on type
            if rule.type == "per_lot":
                commission = volume * rule.value
            elif rule.type == "per_deal":
                commission = rule.value + (deal_value * rule.percent / 100.0)
            elif rule.type == "percent":
                commission = deal_value * rule.percent / 100.0
            else:
                commission = 0.0
            
            # Apply min/max limits
            commission = max(commission, rule.min_value)
            if rule.max_value is not None:
                commission = min(commission, rule.max_value)
            
            return commission
        
        return 0.0
    
    def can_trade(self) -> bool:
        """Check if accounts in this group can trade."""
        return self.permissions.trade_allowed and not self.permissions.view_only
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert group to dictionary."""
        return {
            "id": self.id,
            "name": self.name,
            "type": self.type,
            "currency": self.currency,
            "leverage_default": self.leverage_default,
            "leverage_max": self.leverage_max,
            "margin_call_level": self.margin_call_level,
            "stop_out_level": self.stop_out_level,
            "permissions": {
                "allowed_symbols": self.permissions.allowed_symbols,
                "max_positions": self.permissions.max_positions,
                "max_orders": self.permissions.max_orders,
                "allow_hedging": self.permissions.allow_hedging,
                "allow_short_selling": self.permissions.allow_short_selling,
                "allow_pending_orders": self.permissions.allow_pending_orders,
                "deposit_allowed": self.permissions.deposit_allowed,
                "withdraw_allowed": self.permissions.withdraw_allowed,
                "trade_allowed": self.permissions.trade_allowed,
                "view_only": self.permissions.view_only,
                "internal_only": self.permissions.internal_only,
                "negative_balance_protection": 
                    self.permissions.negative_balance_protection,
            },
            "commissions": [
                {
                    "id": c.id,
                    "type": c.type,
                    "symbol_group": c.symbol_group,
                    "value": c.value,
                    "currency": c.currency,
                    "percent": c.percent,
                }
                for c in self.commissions
            ],
            "swaps": {
                "calculation_mode": self.swaps.calculation_mode,
                "rollover_time": self.swaps.rollover_time,
                "triple_swap_day": self.swaps.triple_swap_day,
            },
            "routing": {
                "default_mode": self.routing.default_mode,
                "a_book_threshold_lots": self.routing.a_book_threshold_lots,
                "lp_priority": self.routing.lp_priority,
            },
            "contest_duration_days": self.contest_duration_days,
            "virtual_balance": self.virtual_balance,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
            "is_active": self.is_active,
        }


@dataclass
class Account:
    """
    Account Entity
    
    Represents a trading account assigned to a Group.
    The Group dictates all rules and permissions for this account.
    """
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    login: int = 0  # Unique login number
    password_hash: str = ""
    investor_password_hash: str = ""
    
    # Identity
    email: str = ""
    phone: str = ""
    full_name: str = ""
    
    # Group assignment (critical - defines all rules)
    group_id: str = ""
    group: Optional[Group] = None  # Loaded from repository
    
    # Account state
    account_type: AccountType = AccountType.REAL
    currency: str = "USD"
    balance: float = 0.0
    equity: float = 0.0
    margin: float = 0.0
    free_margin: float = 0.0
    margin_level: float = 0.0
    
    # Leverage (can be overridden from group default)
    leverage: int = 100
    
    # State flags
    is_enabled: bool = True
    is_online: bool = False
    last_login: Optional[datetime] = None
    registration_date: datetime = field(default_factory=datetime.utcnow)
    
    # Color coding for dealer UI
    color_tag: Optional[str] = None  # e.g., "red" for toxic, "green" for VIP
    
    # Dealer notes
    dealer_notes: str = ""
    
    # Contest-specific
    contest_start: Optional[datetime] = None
    contest_end: Optional[datetime] = None
    
    # Metadata
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime = field(default_factory=datetime.utcnow)
    
    def update_equity(self, unrealized_pnl: float) -> None:
        """Update equity based on unrealized P&L."""
        self.equity = self.balance + unrealized_pnl
        self.free_margin = self.equity - self.margin
        
        if self.margin > 0:
            self.margin_level = self.equity / self.margin
        else:
            self.margin_level = 0.0
    
    def check_margin_call(self) -> bool:
        """Check if margin call level is reached."""
        if self.group and self.margin_level < self.group.margin_call_level:
            return True
        return False
    
    def check_stop_out(self) -> bool:
        """Check if stop out level is reached."""
        if self.group and self.margin_level < self.group.stop_out_level:
            return True
        return False
    
    def can_open_position(self, symbol: str, volume: float, 
                          required_margin: float) -> tuple:
        """
        Check if account can open a position.
        Returns (can_open: bool, reason: str)
        """
        if not self.is_enabled:
            return False, "Account is disabled"
        
        if not self.group:
            return False, "No group assigned"
        
        if not self.group.can_trade():
            return False, "Trading not allowed for this account"
        
        if not self.group.is_symbol_allowed(symbol):
            return False, f"Symbol {symbol} not allowed for this account"
        
        if required_margin > self.free_margin:
            return False, "Insufficient free margin"
        
        # Check max positions
        # (would need to query current positions count)
        
        return True, "OK"
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert account to dictionary."""
        return {
            "id": self.id,
            "login": self.login,
            "email": self.email,
            "phone": self.phone,
            "full_name": self.full_name,
            "group_id": self.group_id,
            "group_name": self.group.name if self.group else None,
            "account_type": self.account_type.value,
            "currency": self.currency,
            "balance": self.balance,
            "equity": self.equity,
            "margin": self.margin,
            "free_margin": self.free_margin,
            "margin_level": self.margin_level,
            "leverage": self.leverage,
            "is_enabled": self.is_enabled,
            "is_online": self.is_online,
            "last_login": self.last_login.isoformat() if self.last_login else None,
            "registration_date": self.registration_date.isoformat(),
            "color_tag": self.color_tag,
            "dealer_notes": self.dealer_notes,
            "contest_start": self.contest_start.isoformat() 
                if self.contest_start else None,
            "contest_end": self.contest_end.isoformat() 
                if self.contest_end else None,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }
