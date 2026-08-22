# Domain Models

Pure business logic with no I/O, database dependencies, or framework coupling.

## Structure

```
domain/
├── models/                # Immutable dataclasses (Order, Position, Deal)
├── groups/                # Group configs (Leverage, Margin Call/Stop Out %)
├── symbols/               # Symbol specs (Digits, Contract Size, Sessions)
├── risk/                  # Pre-trade margin checks, Exposure aggregation
└── routing/               # Chain-of-Responsibility rule engine (A/B book)
```

## Design Principles

1. **Immutability**: All domain objects are immutable dataclasses
2. **No I/O**: No database calls, HTTP requests, or file operations
3. **Pure Functions**: Business logic is deterministic and testable
4. **Value Objects**: Use fixed-point arithmetic for prices/quantities
5. **Protocol Agnostic**: Independent of gRPC/Protobuf (mapping layer in adapters)

## Core Domain Concepts

### Order Lifecycle
```
NEW → PENDING_NEW → ACCEPTED → (PARTIALLY_FILLED)* → FILLED
                          ↓
                    REJECTED / CANCELLED
                    
A-Book specific:
ACCEPTED → PENDING_DEALER → DEALER_APPROVED → FILLED
                        ↓
                  DEALER_REJECTED
```

### Position Modes
- **Hedge Mode**: Multiple positions per symbol (long + short simultaneously)
- **Netting Mode**: Single position per symbol (netted volume/direction)

### A/B Book Routing
- **B-Book**: Internal dealer risk (client loses = broker wins)
- **A-Book**: External hedge to liquidity provider (STP/Agency model)
- **Hybrid**: Threshold-based routing (small orders B-book, large orders A-book)

## Testing Strategy

All domain logic must have 100% unit test coverage:
```bash
pytest tests/unit/domain/ --cov=domain --cov-fail-under=100
```

Tests should be:
- Fast (< 1ms per test)
- Isolated (no shared state)
- Deterministic (no randomness, no timestamps unless mocked)
