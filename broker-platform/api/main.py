"""
FastAPI Main Entrypoint - Broker Platform REST & WebSocket Server

Assembles FastAPI application, registers REST routers, WebSocket routes,
CORS middleware, health check endpoints, and dependency injection providers.
"""
import logging
from typing import Any, Dict, Optional
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.di_providers import register_di_providers
from api.routers import account, auth, trade
from api.routers.admin import admin_router
from api.websockets import endpoints as ws_endpoints
from api.websockets.event_bridge import WebSocketEventBridge

logger = logging.getLogger(__name__)


def create_app(container: Optional[Dict[str, Any]] = None) -> FastAPI:
    """FastAPI application factory function."""
    if container:
        register_di_providers(container)

    app = FastAPI(
        title="Broker Platform API",
        description="Tier-1 Institutional Brokerage REST & WebSocket API",
        version="1.0.0"
    )

    # CORS configuration for Admin UI (Eclipse Theia) and Client Terminals
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # Restrict origins in production
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Include REST Routers
    app.include_router(auth.router)
    app.include_router(trade.router)
    app.include_router(account.router)
    app.include_router(admin_router.router)

    # Include WebSocket Routes
    app.include_router(ws_endpoints.router)

    @app.get("/health", tags=["Health"])
    async def health_check():
        """Health check endpoint for container orchestrators."""
        return {
            "status": "healthy",
            "service": "broker-platform-api",
            "version": "1.0.0"
        }

    return app


app = create_app()
