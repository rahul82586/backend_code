"""
Core Execution Domain Models.

This module defines the entities for Smart Order Routing (SOR),
Dealer Workflow, and Coverage Accounts (Risk Accounts).

Architectural Purpose:
Encapsulates the logic for WHERE an order should be executed (A-Book vs B-Book)
and HOW manual dealer interventions are handled.
"""
from dataclasses import dataclass, field
from datetime import datetime
from decimal import Decimal
from enum import Enum
from typing import Dict, List, Optional


class ExecutionDestination(Enum):
    """
    Target destination for order execution.
    Mirrors MT5 Execution Modes and Centroid Taker Execution Models.
    """
    A_BOOK = "A_BOOK"             # Route to external LP via gateway
    B_BOOK = "B_BOOK"             # Internalize — broker is counterparty
    IN_HOUSE_ECN = "IN_HOUSE_ECN" # Match client vs client internally (CLOB)
    TO_DEALER = "TO_DEALER"       # Manual dealer confirmation required
    REJECT = "REJECT"             # Block the order immediately


@dataclass
class RoutingRule:
    """
    Mirrors MT5 IMTConRoute. Evaluated in priority order (highest first).
    First matching rule wins.
    
    Attributes:
        rule_id: Unique identifier for the rule.
        priority: Higher value = evaluated first.
        group_filter: Group name or None (match all groups).
        symbol_filter: Symbol name or None (match all symbols).
        volume_min: Minimum volume to trigger this rule.
        volume_max: Maximum volume to trigger this rule.
        destination: Where to send the order if matched.
        gateway_id: Specific LP gateway ID (required for A_BOOK).
        is_enabled: Active status of the rule.
    """
    rule_id: str
    priority: int
    destination: ExecutionDestination
    
    # Filters (None = match all)
    group_filter: Optional[str] = None
    symbol_filter: Optional[str] = None
    volume_min: Optional[Decimal] = None
    volume_max: Optional[Decimal] = None
    
    # Action details
    gateway_id: Optional[str] = None
    is_enabled: bool = True


@dataclass
class CoverageAccount:
    """
    Mirrors Centroid 'Risk Account'. Tracks broker's net exposure
    from B-Book trades. Used for hedging decisions.
    
    Attributes:
        account_id: Unique internal ID for the coverage account.
        name: Human-readable name (e.g., "EURUSD_Hedge_Account").
        currency: Account currency.
        net_exposure: {symbol: net_volume}. 
            Positive = broker is long (clients are net short).
            Negative = broker is short (clients are net long).
        margin_level: Current margin level percentage.
        trading_state: NEUTRAL, MARGIN_CALL, STOPPED_OUT.
    """
    account_id: str
    name: str
    currency: str
    
    # Net exposure per symbol: {symbol: net_volume}
    net_exposure: Dict[str, Decimal] = field(default_factory=dict)
    
    margin_level: Decimal = Decimal('0')
    trading_state: str = "NEUTRAL"  # NEUTRAL, MARGIN_CALL, STOPPED_OUT

    def update_exposure(self, symbol: str, volume_delta: Decimal):
        """
        Updates net exposure for a symbol.
        volume_delta > 0: Client bought (Broker sold/shorted exposure).
        volume_delta < 0: Client sold (Broker bought/long exposure).
        """
        current = self.net_exposure.get(symbol, Decimal('0'))
        self.net_exposure[symbol] = current + volume_delta

    def get_total_exposure(self) -> Decimal:
        """Returns absolute total exposure across all symbols."""
        return sum(abs(v) for v in self.net_exposure.values())


@dataclass
class ExecutionInstruction:
    """
    The result of the Smart Order Router.
    Tells the Execution Orchestrator exactly what to do.
    """
    destination: ExecutionDestination
    rule_id: str
    gateway_id: Optional[str] = None
    reason: Optional[str] = None


@dataclass
class DealerDecision:
    """
    Represents a dealer's manual intervention decision.
    Mirrors MT5 DealerAnswer.
    """
    dealer_id: str
    order_ticket: str
    action: str  # CONFIRM, REJECT, REQUOTE
    requote_price: Optional[Decimal] = None
    reason: Optional[str] = None
    decided_at: datetime = field(default_factory=datetime.utcnow)
