"""
Core Ports - Interface Contracts

These interfaces define the contracts that infrastructure adapters must implement.
The core domain depends only on these abstractions, not concrete implementations.
"""
from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional
from datetime import datetime


class IMatchingEngine(ABC):
    """Interface for the matching engine (CLOB / In-house ECN)."""
    
    @abstractmethod
    def submit_order(self, order: Any) -> bool:
        """Submit an order to the matching engine."""
        pass
    
    @abstractmethod
    def cancel_order(self, order_id: str) -> bool:
        """Cancel an existing order."""
        pass
    
    @abstractmethod
    def modify_order(self, order_id: str, new_price: Optional[float] = None, 
                     new_volume: Optional[float] = None) -> bool:
        """Modify an existing order."""
        pass
    
    @abstractmethod
    def get_order_book(self, symbol: str) -> Dict[str, List]:
        """Get the current order book (DOM) for a symbol."""
        pass
    
    @abstractmethod
    def get_best_bid_ask(self, symbol: str) -> tuple:
        """Get the best bid and ask prices."""
        pass


class ILiquidityGateway(ABC):
    """Interface for LP connections (FIX, REST, Ultency-style)."""
    
    @abstractmethod
    def connect(self) -> bool:
        """Establish connection to liquidity provider."""
        pass
    
    @abstractmethod
    def disconnect(self) -> bool:
        """Disconnect from liquidity provider."""
        pass
    
    @abstractmethod
    def send_order(self, order: Any) -> str:
        """Send order to LP and return external order ID."""
        pass
    
    @abstractmethod
    def cancel_order(self, external_order_id: str) -> bool:
        """Cancel order at LP."""
        pass
    
    @abstractmethod
    def get_position(self, symbol: str) -> float:
        """Get current position at LP."""
        pass
    
    @abstractmethod
    def is_connected(self) -> bool:
        """Check if connected to LP."""
        pass


class IMarketDataFeed(ABC):
    """Interface for price aggregators and market data feeds."""
    
    @abstractmethod
    def subscribe(self, symbols: List[str]) -> bool:
        """Subscribe to market data for symbols."""
        pass
    
    @abstractmethod
    def unsubscribe(self, symbols: List[str]) -> bool:
        """Unsubscribe from market data."""
        pass
    
    @abstractmethod
    def get_last_tick(self, symbol: str) -> Optional[Dict]:
        """Get the last tick for a symbol."""
        pass
    
    @abstractmethod
    def get_historical_ticks(self, symbol: str, start: datetime, 
                             end: datetime) -> List[Dict]:
        """Get historical ticks for a symbol."""
        pass
    
    @abstractmethod
    def register_callback(self, callback: callable) -> None:
        """Register callback for real-time tick updates."""
        pass


class IRepository(ABC):
    """Interface for persistence (SQL/NoSQL repositories)."""
    
    @abstractmethod
    def save(self, entity: Any) -> bool:
        """Save an entity."""
        pass
    
    @abstractmethod
    def find_by_id(self, entity_id: str) -> Optional[Any]:
        """Find entity by ID."""
        pass
    
    @abstractmethod
    def find_all(self, filters: Optional[Dict] = None) -> List[Any]:
        """Find all entities with optional filters."""
        pass
    
    @abstractmethod
    def update(self, entity: Any) -> bool:
        """Update an entity."""
        pass
    
    @abstractmethod
    def delete(self, entity_id: str) -> bool:
        """Delete an entity."""
        pass
    
    @abstractmethod
    def begin_transaction(self) -> Any:
        """Begin a database transaction."""
        pass
    
    @abstractmethod
    def commit_transaction(self, transaction: Any) -> bool:
        """Commit a transaction."""
        pass
    
    @abstractmethod
    def rollback_transaction(self, transaction: Any) -> bool:
        """Rollback a transaction."""
        pass


class IEventBus(ABC):
    """Interface for domain events messaging."""
    
    @abstractmethod
    def publish(self, event: Any) -> bool:
        """Publish a domain event."""
        pass
    
    @abstractmethod
    def subscribe(self, event_type: str, handler: callable) -> bool:
        """Subscribe to a specific event type."""
        pass
    
    @abstractmethod
    def unsubscribe(self, event_type: str, handler: callable) -> bool:
        """Unsubscribe from an event type."""
        pass
    
    @abstractmethod
    def publish_batch(self, events: List[Any]) -> bool:
        """Publish multiple events in a batch."""
        pass


class IClusterSync(ABC):
    """Interface for node synchronization and heartbeats."""
    
    @abstractmethod
    def register_node(self, node_id: str, role: str, endpoint: str) -> bool:
        """Register a node in the cluster."""
        pass
    
    @abstractmethod
    def deregister_node(self, node_id: str) -> bool:
        """Deregister a node from the cluster."""
        pass
    
    @abstractmethod
    def get_active_nodes(self) -> List[Dict]:
        """Get list of active nodes."""
        pass
    
    @abstractmethod
    def send_heartbeat(self, node_id: str) -> bool:
        """Send heartbeat for a node."""
        pass
    
    @abstractmethod
    def check_sync_status(self, source_node: str, target_node: str) -> Dict:
        """Check synchronization status between two nodes."""
        pass
    
    @abstractmethod
    def trigger_sync(self, source_node: str, target_node: str, 
                     sync_type: str = "incremental") -> bool:
        """Trigger synchronization between nodes."""
        pass
    
    @abstractmethod
    def acquire_lock(self, resource_id: str, node_id: str, 
                     ttl_seconds: int = 30) -> bool:
        """Acquire distributed lock on a resource."""
        pass
    
    @abstractmethod
    def release_lock(self, resource_id: str, node_id: str) -> bool:
        """Release distributed lock."""
        pass


class INotificationService(ABC):
    """Interface for notifications (Email, SMS, Push, Telegram)."""
    
    @abstractmethod
    def send_email(self, to: str, subject: str, body: str) -> bool:
        """Send email notification."""
        pass
    
    @abstractmethod
    def send_sms(self, phone: str, message: str) -> bool:
        """Send SMS notification."""
        pass
    
    @abstractmethod
    def send_push(self, user_id: str, title: str, message: str) -> bool:
        """Send push notification."""
        pass
    
    @abstractmethod
    def send_telegram(self, chat_id: str, message: str) -> bool:
        """Send Telegram notification."""
        pass
    
    @abstractmethod
    def broadcast_news(self, title: str, content: str, 
                       priority: str = "normal") -> bool:
        """Broadcast news to all connected clients."""
        pass


class ISecurityManager(ABC):
    """Interface for security (SSL, JWT, OAuth, 2FA)."""
    
    @abstractmethod
    def generate_jwt_token(self, user_id: str, roles: List[str], 
                           expires_in_minutes: int = 30) -> str:
        """Generate JWT access token."""
        pass
    
    @abstractmethod
    def validate_jwt_token(self, token: str) -> Dict:
        """Validate JWT token and return payload."""
        pass
    
    @abstractmethod
    def refresh_jwt_token(self, refresh_token: str) -> str:
        """Refresh JWT token."""
        pass
    
    @abstractmethod
    def verify_2fa(self, user_id: str, code: str) -> bool:
        """Verify 2FA code."""
        pass
    
    @abstractmethod
    def setup_2fa(self, user_id: str) -> str:
        """Setup 2FA and return secret key."""
        pass
    
    @abstractmethod
    def check_ip_whitelist(self, ip_address: str, user_id: str) -> bool:
        """Check if IP is whitelisted for user."""
        pass
    
    @abstractmethod
    def check_antiflood(self, user_id: str, action: str) -> bool:
        """Check rate limiting / antiflood."""
        pass
    
    @abstractmethod
    def renew_certificate(self, node_id: str, cert_type: str) -> bool:
        """Renew SSL certificate for a node."""
        pass
