"""
Core Ports - The Contracts That Enable Swappable Infrastructure

These abstract base classes define the boundaries between the pure domain logic
and external concerns (databases, message brokers, matching engines).
Implementations live in the infrastructure layer and are injected at runtime.
"""
from abc import ABC, abstractmethod
from typing import List, Optional, TypeVar, Generic, Callable
from datetime import datetime

from core.events.domain_events import DomainEvent

T = TypeVar('T')


class IEventBus(ABC):
    """
    Contract for the internal messaging system.
    
    Architectural Purpose:
    Decouples the producer of an event (e.g., OMS Domain) from the consumers 
    (e.g., ClickHouse Writer, AI Agent, Notification Service). 
    Implementations can be Redis, Kafka, or an in-memory queue for testing.
    """
    
    @abstractmethod
    async def publish(self, event: DomainEvent) -> None:
        """
        Publishes a domain event to the specified channel/topic.
        Must be non-blocking (fire-and-forget) to maintain high throughput.
        """
        pass

    @abstractmethod
    async def subscribe(self, channel: str, callback: Callable[[dict], None]) -> None:
        """
        Subscribes to a specific channel and invokes the callback upon message receipt.
        The callback receives a deserialized dictionary representation of the event.
        """
        pass

    @abstractmethod
    async def disconnect(self) -> None:
        """
        Gracefully closes connections and cleans up resources.
        """
        pass


class IOrderRepository(ABC, Generic[T]):
    """
    Contract for Order persistence.
    
    Architectural Purpose:
    Hides the database technology (PostgreSQL, MongoDB, etc.) from the Domain.
    The OMS domain logic calls save() or find_by_id(), unaware of SQL or ORM.
    This enables swapping databases without touching core business logic.
    """
    
    @abstractmethod
    async def save(self, order: T) -> T:
        """
        Persists an order aggregate. Handles both inserts and updates.
        Returns the persisted object (often with updated DB IDs).
        """
        pass

    @abstractmethod
    async def find_by_id(self, order_id: str) -> Optional[T]:
        """
        Retrieves an order by its unique identifier.
        Returns None if not found.
        """
        pass

    @abstractmethod
    async def find_active_orders_by_account(self, account_id: str) -> List[T]:
        """
        Retrieves all open/pending orders for a specific account.
        Crucial for risk checks and UI display.
        """
        pass

    @abstractmethod
    async def get_next_ticket_id(self) -> str:
        """
        Generates a unique, sequential ticket ID (MT5 style).
        Implementation must ensure thread-safety/atomicity.
        """
        pass


class IMatchingEngine(ABC, Generic[T]):
    """
    Contract for the core trading logic.
    
    Architectural Purpose:
    Defines how orders are processed against the market.
    Allows swapping the engine implementation (e.g., Python prototype -> Rust PyO3 module)
    via Dependency Injection without changing the OMS domain logic.
    """
    
    @abstractmethod
    async def submit_order(self, order: T) -> None:
        """
        Submits an order to the engine for processing.
        Triggers immediate matching logic or queues it.
        """
        pass

    @abstractmethod
    async def cancel_order(self, order_id: str) -> bool:
        """
        Attempts to cancel an existing order.
        Returns True if successful, False otherwise.
        """
        pass

    @abstractmethod
    async def modify_order(self, order_id: str, new_price: float, new_quantity: int) -> bool:
        """
        Modifies an existing order (Price/Quantity).
        In strict FIFO engines, this might be implemented as Cancel+Replace.
        """
        pass

    @abstractmethod
    def get_market_state(self, symbol: str) -> dict:
        """
        Returns the current state of the order book for a symbol.
        Used for pre-trade checks and visibility.
        """
        pass


class ILiquidityGateway(ABC, Generic[T]):
    """
    Port for external Liquidity Provider (LP) connectivity.
    
    Architectural Purpose:
    Abstracts away the specific protocol (FIX, REST, WebSocket) used to 
    communicate with external LPs (LMAX, Binance, Centroid, etc.).
    Allows adding/removing LPs without changing core execution logic.
    """
    
    @abstractmethod
    async def send_order(self, order: T, gateway_id: str) -> dict:
        """
        Sends an order to an external LP.
        Returns an execution report/acknowledgment.
        """
        pass
    
    @abstractmethod
    async def cancel_order(self, order_id: str, gateway_id: str) -> bool:
        """
        Cancels an order at the external LP.
        Returns True if successful.
        """
        pass
    
    @abstractmethod
    async def get_quotes(self, symbols: list[str]) -> dict[str, dict]:
        """
        Fetches current bid/ask quotes for multiple symbols.
        Returns {symbol: {bid, ask, timestamp}}.
        """
        pass


class ICoverageAccountRepository(ABC, Generic[T]):
    """
    Contract for Coverage Account (Risk Account) persistence.
    
    Architectural Purpose:
    Manages the broker's internal hedge accounts used to offset B-Book exposure.
    Critical for risk management and regulatory reporting.
    """
    
    @abstractmethod
    async def find_by_id(self, account_id: str) -> Optional[T]:
        """Retrieves a coverage account by ID."""
        pass
    
    @abstractmethod
    async def save(self, account: T) -> T:
        """Persists a coverage account."""
        pass
    
    @abstractmethod
    async def update_exposure(
        self, 
        account_id: str, 
        symbol: str, 
        volume_delta: 'Decimal'
    ) -> None:
        """
        Updates net exposure for a symbol.
        volume_delta > 0: Client bought (Broker sold).
        volume_delta < 0: Client sold (Broker bought).
        """
        pass


class IRoutingRuleRepository(ABC, Generic[T]):
    """
    Contract for Routing Rule persistence.
    
    Architectural Purpose:
    Manages the dynamic routing rules that determine A-Book vs B-Book allocation.
    Rules can be updated at runtime without restarting the server.
    """
    
    @abstractmethod
    async def get_active_rules(self) -> List[T]:
        """Returns all enabled routing rules sorted by priority."""
        pass
    
    @abstractmethod
    async def save(self, rule: T) -> T:
        """Creates or updates a routing rule."""
        pass
    
    @abstractmethod
    async def delete(self, rule_id: str) -> bool:
        """Deletes a routing rule."""
        pass
