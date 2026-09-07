from decimal import Decimal
from typing import List, Optional
from datetime import datetime, timezone

from .models import MarginSnapshot, RiskStatus
from ..accounts.models import Account
from ..oms.entities.position import Position
from ...ports.interfaces import ISymbolRepository, IMarketDataFeed


class RiskEngine:
    """
    Pure domain logic for risk calculations.
    
    Architectural Purpose:
    Encapsulates all margin and stop-out logic. Uses MarketDataEngine or IMarketDataFeed
    for current market price lookup.
    
    MT5 Compliance:
    - Margin Level = (Equity / Margin Used) × 100
    - Stop Out: Closes worst-loss positions first until margin recovers
    """
    
    def __init__(self, symbol_repo: ISymbolRepository, market_data_engine: Any):
        self.symbol_repo = symbol_repo
        self.market_data_engine = market_data_engine

    def _get_bid(self, symbol: str) -> Decimal:
        """Helper to resolve bid price from MarketDataEngine or legacy feed."""
        if hasattr(self.market_data_engine, 'get_latest_tick'):
            tick = self.market_data_engine.get_latest_tick(symbol)
            if tick:
                return tick.bid
        if hasattr(self.market_data_engine, 'get_bid'):
            return self.market_data_engine.get_bid(symbol)
        raise ValueError(f"No market data available for symbol {symbol}")

    def _get_ask(self, symbol: str) -> Decimal:
        """Helper to resolve ask price from MarketDataEngine or legacy feed."""
        if hasattr(self.market_data_engine, 'get_latest_tick'):
            tick = self.market_data_engine.get_latest_tick(symbol)
            if tick:
                return tick.ask
        if hasattr(self.market_data_engine, 'get_ask'):
            return self.market_data_engine.get_ask(symbol)
        raise ValueError(f"No market data available for symbol {symbol}")

    def calculate_margin_level(self, account: Account, positions: List[Position]) -> MarginSnapshot:
        """
        Calculate real-time margin level for an account.
        
        Formula: MarginLevel = (Equity / MarginUsed) × 100
        If MarginUsed == 0, return infinity (no risk).
        """
        unrealized_pnl = Decimal('0')
        margin_used = Decimal('0')
        
        for position in positions:
            try:
                symbol_info = self.symbol_repo.get_symbol(position.symbol)
                
                # Get current market price based on position side
                if position.side.name == "BUY":
                    current_price = self._get_bid(position.symbol)
                    pnl_per_unit = current_price - position.average_price.value
                else:  # SELL
                    current_price = self._get_ask(position.symbol)
                    pnl_per_unit = position.average_price.value - current_price

                
                # PnL = price_diff * volume * contract_size
                position_pnl = pnl_per_unit * position.volume.value * symbol_info.contract_size
                unrealized_pnl += position_pnl
                
                # Margin = (Price * Volume * ContractSize) / Leverage
                margin_for_position = (current_price * position.volume.value * symbol_info.contract_size) / Decimal(str(account.group.margin.leverage))
                margin_used += margin_for_position
                
            except Exception as e:
                # Log but continue with other positions
                pass
        
        equity = account.balance.amount + unrealized_pnl
        margin_free = equity - margin_used
        
        # Calculate margin level
        if margin_used == Decimal('0'):
            margin_level = Decimal('inf')
        else:
            margin_level = (equity / margin_used) * Decimal('100')
        
        # Determine risk status based on Group rules
        margin_call_level = Decimal(str(account.group.margin.margin_call_level))
        stop_out_level = Decimal(str(account.group.margin.stop_out_level))
        
        if margin_level < stop_out_level:
            status = RiskStatus.STOPPED_OUT
        elif margin_level < margin_call_level:
            status = RiskStatus.MARGIN_CALL
        else:
            status = RiskStatus.NORMAL
        
        return MarginSnapshot(
            account_login=account.login_id,
            balance=account.balance.amount,
            equity=equity,
            margin_used=margin_used,
            margin_free=margin_free,
            margin_level=margin_level,
            status=status
        )

    def detect_margin_call(self, account: Account, snapshot: MarginSnapshot) -> bool:
        """
        Check if account has breached margin call threshold.
        
        Returns:
            True if margin_level < account.group.margin.margin_call_level
        """
        margin_call_level = Decimal(str(account.group.margin.margin_call_level))
        return snapshot.margin_level < margin_call_level

    def detect_stop_out(self, account: Account, snapshot: MarginSnapshot) -> bool:
        """
        Check if account has breached stop-out threshold.
        
        Returns:
            True if margin_level < account.group.margin.stop_out_level
        """
        stop_out_level = Decimal(str(account.group.margin.stop_out_level))
        return snapshot.margin_level < stop_out_level

    def select_positions_for_liquidation(
        self, 
        positions: List[Position], 
        target_margin_level: Decimal,
        current_equity: Decimal,
        symbol_repo: ISymbolRepository,
        market_feed: IMarketDataFeed
    ) -> List[Position]:
        """
        Select positions to close during Stop Out.
        
        MT5 behavior: Close worst-loss positions first until margin level 
        recovers above stop_out_level.
        
        Args:
            positions: All open positions for the account
            target_margin_level: The margin level to recover to
            current_equity: Current account equity
            symbol_repo: To get contract sizes
            market_feed: To get current prices
            
        Returns:
            Ordered list of positions to close (worst first)
        """
        # Calculate current PnL for each position to determine worst performers
        positions_with_pnl = []
        
        for position in positions:
            try:
                symbol_info = symbol_repo.get_symbol(position.symbol)
                
                feed = market_feed if market_feed is not None else self.market_data_engine
                if position.side.name == "BUY":
                    if hasattr(feed, 'get_latest_tick'):
                        t = feed.get_latest_tick(position.symbol)
                        current_price = t.bid if t else Decimal('0')
                    else:
                        current_price = feed.get_bid(position.symbol)
                    pnl = (current_price - position.average_price.value) * position.volume.value * symbol_info.contract_size
                else:
                    if hasattr(feed, 'get_latest_tick'):
                        t = feed.get_latest_tick(position.symbol)
                        current_price = t.ask if t else Decimal('0')
                    else:
                        current_price = feed.get_ask(position.symbol)
                    pnl = (position.average_price.value - current_price) * position.volume.value * symbol_info.contract_size
                
                positions_with_pnl.append((position, pnl))
            except Exception:
                continue
        
        # Sort by PnL ascending (worst losses first)
        positions_with_pnl.sort(key=lambda x: x[1])
        
        # Return positions ordered by worst PnL first
        return [pos for pos, pnl in positions_with_pnl]
