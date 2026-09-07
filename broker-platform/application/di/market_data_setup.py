"""
Market Data Dependency Injection Container & Setup Factory

Assembles and wires the full Market Data Layer pipeline:
MockTickFeed → TickIngestor → MarketDataEngine → RedisMarketDataCache & BarRepository.

Architectural Rule: Application DI factory.
"""
import logging
from typing import Any, Dict, List, Optional

from application.services.market_data_subscriptions import MarketDataSubscriptions
from application.services.tick_ingestor import TickIngestor
from core.domains.market_data.engine import MarketDataEngine
from core.ports.interfaces import IBarRepository, IEventBus
from infrastructure.feeds.mock_feed import MockTickFeed
from infrastructure.persistence.redis_market_data import RedisMarketDataCache

logger = logging.getLogger(__name__)


def setup_market_data(
    event_bus: IEventBus,
    symbols: Optional[List[str]] = None,
    redis_client: Optional[Any] = None,
    bar_repository: Optional[IBarRepository] = None
) -> Dict[str, Any]:
    """
    Factory function to wire and return all market data layer components.
    """
    if symbols is None:
        symbols = ["EURUSD", "GBPUSD", "USDJPY", "XAUUSD", "BTCUSD"]

    redis_cache = RedisMarketDataCache(redis_client) if redis_client else None

    engine = MarketDataEngine(
        event_bus=event_bus,
        redis_cache=redis_cache,
        bar_repository=bar_repository
    )

    mock_feed = MockTickFeed(symbols=symbols)
    ingestor = TickIngestor(market_data_engine=engine, feeds=[mock_feed])
    subscriptions = MarketDataSubscriptions(event_bus=event_bus, market_data_engine=engine)

    logger.info("Market Data Layer components successfully assembled via DI container.")

    return {
        "engine": engine,
        "ingestor": ingestor,
        "subscriptions": subscriptions,
        "redis_cache": redis_cache,
        "mock_feed": mock_feed
    }
