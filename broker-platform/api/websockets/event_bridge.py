"""
WebSocket Event Bridge Service

Subscribes to IEventBus domain events and bridges them to the WebSocket ConnectionManager.
Connects internal domain events (ticks, deals, margin calls) to real-time client WebSocket streams.

Architectural Rule: Event-to-WebSocket bridge service.
"""
import logging
from typing import Dict, Any

from api.websockets.manager import ConnectionManager
from core.events.domain_events import EventType
from core.ports.interfaces import IEventBus

logger = logging.getLogger(__name__)


class WebSocketEventBridge:
    """
    Subscribes to IEventBus channels and dispatches payloads to public/private WebSockets.
    """
    def __init__(self, event_bus: IEventBus, connection_manager: ConnectionManager):
        self.event_bus = event_bus
        self.manager = connection_manager

    async def register(self) -> None:
        """Subscribe event handlers to IEventBus channels."""
        await self.event_bus.subscribe(EventType.TICK_RECEIVED.value, self._handle_tick)
        await self.event_bus.subscribe(EventType.BOOK_UPDATED.value, self._handle_book)
        await self.event_bus.subscribe(EventType.DEAL_CREATED.value, self._handle_user_event)
        await self.event_bus.subscribe(EventType.ORDER_REJECTED.value, self._handle_user_event)
        await self.event_bus.subscribe(EventType.MARGIN_CALL_TRIGGERED.value, self._handle_user_event)
        await self.event_bus.subscribe(EventType.STOP_OUT_INITIATED.value, self._handle_user_event)
        logger.info("WebSocketEventBridge successfully registered to IEventBus channels.")

    async def _handle_tick(self, event_dict: Dict[str, Any]) -> None:
        """Bridge TICK_RECEIVED domain event to public broadcast stream."""
        payload = event_dict.get("payload", {})
        symbol = payload.get("symbol", "")
        bid = payload.get("bid", "0")
        ask = payload.get("ask", "0")
        spread = payload.get("spread", "0")
        await self.manager.broadcast_tick(symbol=symbol, bid=bid, ask=ask, spread=spread)

    async def _handle_book(self, event_dict: Dict[str, Any]) -> None:
        """Bridge BOOK_UPDATED domain event to public broadcast stream."""
        payload = event_dict.get("payload", {})
        symbol = payload.get("symbol", "")
        best_bid = payload.get("best_bid", "0")
        best_ask = payload.get("best_ask", "0")
        spread = payload.get("spread", "0")
        await self.manager.broadcast_tick(symbol=symbol, bid=best_bid, ask=best_ask, spread=spread)

    async def _handle_user_event(self, event_dict: Dict[str, Any]) -> None:
        """Bridge trade and risk domain events to private user WebSocket streams."""
        event_type = event_dict.get("event_type", "user_update")
        payload = event_dict.get("payload", {})
        user_id = payload.get("account_login") or payload.get("login_id") or payload.get("account_id")

        if user_id:
            await self.manager.send_user_update(user_id=user_id, event_type=event_type, payload=payload)
