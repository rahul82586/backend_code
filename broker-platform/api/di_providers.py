"""
FastAPI Dependency Injection Providers

Container factory functions exposing instantiated application command handlers,
query handlers, repositories, and domain services to FastAPI routes via Depends().

Architectural Rule: Decouples API endpoints from concrete infrastructure instantiations.
"""
from typing import Any, Optional

# Container storage for application instances initialized at app startup
_container: dict[str, Any] = {}


def register_di_providers(providers: dict[str, Any]) -> None:
    """Register runtime dependencies (repos, handlers, engines) into global container."""
    _container.update(providers)


def get_account_repo() -> Any:
    """Provider for IAccountRepository."""
    repo = _container.get("account_repo")
    if not repo:
        raise RuntimeError("Account repository not registered in DI container")
    return repo


def get_position_repo() -> Any:
    """Provider for IPositionRepository."""
    repo = _container.get("position_repo")
    if not repo:
        raise RuntimeError("Position repository not registered in DI container")
    return repo


def get_symbol_repo() -> Any:
    """Provider for ISymbolRepository."""
    repo = _container.get("symbol_repo")
    if not repo:
        raise RuntimeError("Symbol repository not registered in DI container")
    return repo


def get_event_bus() -> Any:
    """Provider for IEventBus."""
    bus = _container.get("event_bus")
    if not bus:
        raise RuntimeError("Event bus not registered in DI container")
    return bus


def get_market_data_engine() -> Any:
    """Provider for MarketDataEngine."""
    return _container.get("market_data_engine")


def get_create_order_handler() -> Any:
    """Provider for CreateOrderCommandHandler."""
    handler = _container.get("create_order_handler")
    if not handler:
        raise RuntimeError("CreateOrderCommandHandler not registered in DI container")
    return handler


def get_account_info_query_handler() -> Any:
    """Provider for GetAccountInfoQueryHandler."""
    handler = _container.get("account_info_query_handler")
    if not handler:
        raise RuntimeError("GetAccountInfoQueryHandler not registered in DI container")
    return handler


def get_positions_query_handler() -> Any:
    """Provider for GetPositionsQueryHandler."""
    handler = _container.get("positions_query_handler")
    if not handler:
        raise RuntimeError("GetPositionsQueryHandler not registered in DI container")
    return handler
