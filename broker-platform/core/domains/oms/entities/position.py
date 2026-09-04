from dataclasses import dataclass, field
from datetime import datetime
from decimal import Decimal
from typing import Optional

from core.domains.common.value_objects import Price, Volume, Money
from core.domains.oms.entities.order import OrderType
from core.domains.oms.entities.deal import Deal, DealType

class PositionMode(Enum):
    HEDGING = "HEDGING"
    NETTING = "NETTING"

@dataclass
class Position:
    """
    Aggregate Open State.
    Derived from the sequence of Deals (Buy/Sell) for a specific Symbol.
    
    Architectural Purpose:
    Represents the trader's current exposure.
    Supports both HEDGING (separate positions per direction) and 
    NETTING (aggregated volume) modes as defined by the Account's Group.
    
    CRITICAL FIX: Includes contract_size for accurate PnL calculation.
    """
    id: str  # Usually "{account_login}:{symbol}:{side}" for Hedging
    account_login: str
    symbol: str
    
    volume: Volume
    side: OrderType  # BUY or SELL
    average_price: Price
    contract_size: Decimal  # CRITICAL: Required for correct PnL math
    
    unrealized_pnl: Money = field(default_factory=lambda: Money(Decimal('0'), "USD"))
    swap_accumulated: Money = field(default_factory=lambda: Money(Decimal('0'), "USD"))
    
    opened_at: datetime = field(default_factory=datetime.utcnow)
    deal_count: int = 0  # Number of deals aggregated into this position

    def apply_deal(self, deal: Deal, position_mode: PositionMode = PositionMode.HEDGING) -> Optional['Position']:
        """
        Updates position state based on a new Deal.
        
        Args:
            deal: The executed deal to apply
            position_mode: HEDGING creates new positions, NETTING aggregates
            
        Returns:
            In HEDGING mode with opposite side: Returns NEW position (reversal)
            In NETTING mode: Updates self, returns None
            If closed fully: Sets volume to 0, caller should archive
        """
        if deal.deal_type not in [DealType.BUY, DealType.SELL]:
            return None  # Ignore non-trading deals

        deal_side = OrderType.BUY if deal.deal_type == DealType.BUY else OrderType.SELL
        
        # HEDGING MODE: Every deal creates a new position or adds to same-direction only
        if position_mode == PositionMode.HEDGING:
            if deal_side != self.side:
                # Opposite direction in Hedging = Create NEW position (do not modify self)
                # Caller is responsible for creating the new position object
                return self._handle_hedge_opposite(deal)
            else:
                # Same direction = Add to existing position
                self._add_to_position(deal)
                return None
        
        # NETTING MODE: Aggregate all deals
        else:
            if deal_side == self.side:
                # Adding to position
                self._add_to_position(deal)
                return None
            else:
                # Closing or Reversing
                return self._close_or_reverse(deal)

    def _add_to_position(self, deal: Deal):
        """Adds volume to current position, recalculating average price."""
        total_val = (self.average_price.value * self.volume.value) + \
                    (deal.price.value * deal.volume.value)
        new_vol = self.volume.value + deal.volume.value
        
        self.volume = Volume(new_vol)
        self.average_price = Price(total_val / new_vol)
        self.deal_count += 1

    def _close_or_reverse(self, deal: Deal) -> Optional['Position']:
        """
        Handles closing partial/full or reversing position in Netting mode.
        Returns new Position if reversal occurs.
        """
        if deal.volume.value < self.volume.value:
            # Partial Close
            self.volume = Volume(self.volume.value - deal.volume.value)
            self.deal_count += 1
            return None
            
        elif deal.volume.value == self.volume.value:
            # Full Close
            self.volume = Volume(Decimal('0'))
            self.deal_count += 1
            return None
            
        else:
            # Reverse: Close old, open new opposite
            new_vol = deal.volume.value - self.volume.value
            new_position = Position(
                id=f"{self.account_login}:{self.symbol}:{deal_side.value}",
                account_login=self.account_login,
                symbol=self.symbol,
                volume=Volume(new_vol),
                side=deal_side,
                average_price=deal.price,
                contract_size=self.contract_size,
                opened_at=datetime.utcnow(),
                deal_count=1
            )
            return new_position

    def _handle_hedge_opposite(self, deal: Deal) -> Optional['Position']:
        """
        In Hedging mode, opposite deal creates a NEW separate position.
        Returns the new position object. Self remains unchanged.
        """
        deal_side = OrderType.BUY if deal.deal_type == DealType.BUY else OrderType.SELL
        
        new_position = Position(
            id=f"{self.account_login}:{self.symbol}:{deal_side.value}",
            account_login=self.account_login,
            symbol=self.symbol,
            volume=deal.volume,
            side=deal_side,
            average_price=deal.price,
            contract_size=self.contract_size,
            opened_at=datetime.utcnow(),
            deal_count=1
        )
        return new_position

    def update_unrealized_pnl(self, current_market_price: Price):
        """
        Calculates current floating PnL.
        
        CRITICAL FIX: Now includes contract_size in calculation.
        Formula: (CurrentPrice - AvgPrice) * Volume * ContractSize
        """
        if self.volume.value == 0:
            self.unrealized_pnl = Money(Decimal('0'), "USD")
            return

        diff = current_market_price.value - self.average_price.value
        
        # For SELL positions, profit is when price goes down
        if self.side == OrderType.SELL:
            diff = -diff
        
        # CORRECTED FORMULA: Include contract_size
        # Example: EURUSD, 1 lot (100k), 1 pip move (0.0001)
        # PnL = 0.0001 * 1 * 100000 = $10.00
        pnl_val = diff * self.volume.value * self.contract_size
        self.unrealized_pnl = Money(pnl_val, "USD")

    def is_closed(self) -> bool:
        """Returns True if position volume is zero."""
        return self.volume.value == 0
