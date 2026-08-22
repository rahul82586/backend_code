# 🏛️ ARCHITECTURAL MASTER PLAN: Institutional Brokerage Backend

## 1. Executive Summary

This document outlines the blueprint for a production-grade, MetaTrader 5-equivalent distributed trading backend. It replaces ad-hoc HTTP/JSON communication with a strict, language-agnostic **Protobuf/gRPC** contract. It enforces a **Hot/Cold storage split** (in-memory state + append-only WAL, with async ETL to PostgreSQL) to ensure zero SQL latency on the hot trading path. It natively supports **Centroid-style Maker/Taker routing**, **Risk Accounts**, and **MT5-compliant regulatory reporting** (EMIR/NFA).

---

## 2. Production-Grade Folder Structure

```
broker_platform/
│
├── protocol/                          # ★ THE CONTRACT (Language-Agnostic)
│   ├── proto/                         
│   │   ├── order.proto                # Order, OrderReject, OrderFill events
│   │   ├── tick.proto                 # QuoteTick, TradeTick, OrderBookDelta
│   │   ├── account.proto              # AccountState, MarginCall, StopOut events
│   │   └── report.proto               # EMIR/NFA report generation requests
│   ├── gen_python/                    # Generated Python stubs (grpcio-tools)
│   └── gen_rust/                      # Generated Rust stubs (prost-build)
│
├── domain/                            # ★ PURE BUSINESS LOGIC (No I/O, No DB)
│   ├── models/                        # Immutable dataclasses (Order, Position, Deal)
│   ├── groups/                        # Group configs (Leverage, Hedge/Netting flags, Margin Call/Stop Out %)
│   ├── symbols/                       # Symbol specs (Digits, Contract Size, Sessions, Trade Modes)
│   ├── risk/                          # Pre-trade margin checks, Exposure aggregation math
│   └── routing/                       # Centroid-style Chain-of-Responsibility rule engine
│
├── core_engine/                       # ★ THE HOT PATH (In-Memory, Ultra-Fast)
│   ├── matching/                      # TOB/CLOB execution (implements IMatchingEngine)
│   ├── position_keeper/               # Handles Hedge vs. Netting merging logic
│   ├── journal/                       # ★ Append-only Write-Ahead Log (WAL) (.dat + .idx)
│   └── state_cache/                   # In-memory dict/Redis of live balances, positions, quotes
│
├── services/                          # ★ LONG-RUNNING MICROSERVICES
│   ├── access_service/                # Auth, JWT, Rate Limiting, Anti-DDoS, GeoIP routing
│   ├── oms_service/                   # Order lifecycle, Dealer Queue (PENDING_DEALER state)
│   ├── risk_service/                  # Async background worker: Stop-Outs, Margin Calls, NOP limits
│   ├── matching_service/              # Wraps core_engine, exposes gRPC/TCP IPC
│   └── history_service/               # Tick ingestion, OHLCV aggregation, News parsing
│
├── adapters/                          # ★ EXTERNAL I/O BOUNDARIES
│   ├── feeders/                       # MT5/MT4 Feeder connectors (GatewayAPI64.dll equivalents)
│   ├── gateways/                      # LP connectors (FIX 4.4/5.0, REST, WebSocket)
│   ├── news/                          # AllianceNews, Newsquawk, Financial Source adapters
│   └── ipc/                           # Binary TCP / gRPC transport layer
│
├── plugins/                           # ★ MT5-STYLE SERVER PLUGINS (C++ DLL or Python Hooks)
│   ├── emir_reports/                  # EMIR CME Automated/Manual report generation
│   ├── nfa_reports/                   # NFA compliance reporting, SFTP Outbox/Sent logic
│   └── finteza/                       # Web terminal tracking and analytics hooks
│
├── storage/                           # ★ HOT / COLD / WAREHOUSE SPLIT
│   ├── cold/                          # Append-only binary logs (e.g., confirms/YYYY.MM.DD.trans/*.dat)
│   ├── etl/                           # Async batch processor: cold/ → warehouse (PostgreSQL)
│   └── warehouse/                     # PostgreSQL (Reporting, Admin UI, Regulatory ONLY)
│
├── observability/                     # ★ FIRST-CLASS CITIZEN
│   ├── metrics/                       # Prometheus (orders/sec, p99 latency, queue depth)
│   ├── tracing/                       # OpenTelemetry (trace order: access → routing → journal → ack)
│   └── logging/                       # Structured JSON logging (ELK/Datadog ready)
│
├── deploy/                            # ★ INFRASTRUCTURE AS CODE
│   ├── docker/                        # Dockerfiles for each service
│   ├── compose/                       # docker-compose.yml for local dev
│   └── secrets/                       # Vault / K8s secrets management
│
└── tests/                             # ★ COMPREHENSIVE TESTING
    ├── unit/                          # Domain logic (fast, no I/O)
    ├── integration/                   # IPC, DB, Adapter interactions
    └── load/                          # k6 / Locust scripts (simulate 10k orders/sec)
```

---

## 3. Core Component Specifications (Mapped to MT5/Centroid)

| Component | MT5 / Centroid Equivalent | Responsibility & Rules |
| :--- | :--- | :--- |
| **Access Server** | MT5 Access Server | TLS termination, JWT validation, DDoS protection. Routes internal traffic via gRPC. |
| **Main Trade Server** | MT5 Main Trade Server | **Hot Path Only.** OMS, Pre-trade RMS, Routing Engine, Matching, Position Keeper. **NO PostgreSQL queries here.** |
| **History Server** | MT5 History Server + Data Feeds | Runs `adapters/feeders/` (simulating `feeder64.exe` + `GatewayAPI64.dll`). Handles symbol filtering (`*`, `!`), tick aggregation, and News Feeder ingestion. |
| **Backup Server** | MT5 Backup Server | Monitors Main/History. Writes to `storage/cold/` (WAL). Runs `storage/etl/` to push data to PostgreSQL. |
| **Reporting Plugins** | MT5 `EMIR.Reports64.dll` | Reads from `storage/cold/confirms/`. Generates CSVs, moves them to `Outbox/`, and async uploads to regulator SFTP. Moves to `Sent/` on success. |
| **Risk Accounts** | Centroid Risk Accounts | Master/Slave accounts with Net Open Position (NOP) limits. Auto-hedges to Makers when limits are breached. |
| **Dealer Queue** | MT5 Manager "Dealer" | Orders routed `TO_DEALER` enter a `PENDING_DEALER` state in Redis. Admin UI approves/rejects, triggering OMS resume. |

---

## 4. Network & Protocol Matrix

| Communication Path | Protocol | Purpose |
| :--- | :--- | :--- |
| **Client ↔ Access Server** | WebSocket / HTTPS | JSON/Protobuf over WS for client orders/quotes |
| **Access ↔ Main/History** | **gRPC / Protobuf** | Strict schema, ultra-low latency, language-agnostic |
| **Main ↔ LP Gateways** | FIX 4.4/5.0 or WebSocket | External liquidity provider connectivity |
| **Main ↔ Backup** | NATS / Redis PubSub | Asynchronous event streaming for WAL replication |
| **Internal State** | In-Memory Dicts / Redis | Zero disk I/O for sub-millisecond margin checks |

---

## 5. Extensibility & Dependency Injection (The "VS Code" Model)

To ensure we can swap Python for Rust/C++ later, we strictly use interfaces:

```python
# domain/interfaces/i_matching.py
from typing import Protocol

class IMatchingEngine(Protocol):
    async def submit_order(self, order: Order) -> OrderEvent: ...
    async def cancel_order(self, order_id: str) -> OrderEvent: ...
    async def modify_order(self, order_id: str, new_params: dict) -> OrderEvent: ...

# infrastructure/matching/python_tob.py
class PythonTOBMatchingEngine(IMatchingEngine):
    """Top-of-Book matching engine in Python."""
    async def submit_order(self, order: Order) -> OrderEvent: ...

# infrastructure/matching/rust_clob.py (Future)
class RustCLOBMatchingEngine(IMatchingEngine):
    """Full CLOB matching engine in Rust (via gRPC)."""
    async def submit_order(self, order: Order) -> OrderEvent: ...

# core/di_container.py (The ONLY place concrete classes are bound)
def create_matching_engine() -> IMatchingEngine:
    return PythonTOBMatchingEngine()  # Swap to RustCLOBMatchingEngine() later
```

---

## 6. Hot Path vs Cold Path

### Hot Path (Sub-Millisecond Requirements)
- ✅ In-memory state cache (Redis or dict)
- ✅ Append-only WAL for durability
- ✅ Pre-trade margin checks
- ✅ Order matching/execution
- ✅ Position updates
- ❌ **NO PostgreSQL queries**
- ❌ **NO external HTTP calls**
- ❌ **NO blocking I/O**

### Cold Path (Async, Eventually Consistent)
- ✅ WAL → PostgreSQL ETL (batch processing)
- ✅ Regulatory report generation
- ✅ Admin UI queries
- ✅ Historical tick analysis
- ✅ Account statements

---

## 7. A/B Book Routing Flow

```
Order Submitted
       ↓
┌─────────────────────┐
│  Pre-Trade Checks   │
│  - Margin           │
│  - Symbol Allowed   │
│  - Volume Limits    │
└─────────────────────┘
       ↓
┌─────────────────────┐
│  Routing Engine     │
│  - Volume threshold │
│  - Symbol rules     │
│  - Account group    │
└─────────────────────┘
       ↓
    ┌─┴─┐
    │   │
    v   v
┌───────┐ ┌───────┐
│A-Book │ │B-Book │
│(STP)  │ │(Risk) │
└───────┘ └───────┘
    │         │
    │         v
    │    ┌─────────────┐
    │    │Internal Fill│
    │    └─────────────┘
    │
    v
┌─────────────────┐
│ Dealer Queue?   │──Yes──→ PENDING_DEALER
└─────────────────┘          (await approval)
    │ No
    v
┌─────────────────┐
│ Route to Maker  │
│ (LP Gateway)    │
└─────────────────┘
```

---

## 8. Testing Strategy

| Test Type | Scope | Tools | Target Coverage |
| :--- | :--- | :--- | :--- |
| **Unit Tests** | Domain logic only | pytest | 100% domain/ |
| **Integration Tests** | Service IPC, DB, adapters | pytest + testcontainers | 80% services/ |
| **Load Tests** | Throughput, latency | k6 / Locust | 10k orders/sec |
| **Chaos Tests** | Failure recovery | Chaos Mesh | Critical paths |

---

## 9. Migration Checklist

- [ ] Extract domain models from existing codebase
- [x] Define Protobuf contracts (order.proto, tick.proto, account.proto, report.proto)
- [ ] Implement WAL system (append-only .dat + .idx files)
- [ ] Build gRPC service skeletons
- [ ] Migrate A/B-book routing logic to domain/routing/
- [ ] Implement state cache (Redis wrapper)
- [ ] Build ETL pipeline (WAL → PostgreSQL)
- [ ] Port 29 existing tests to new structure
- [ ] Add load testing suite

---

## 10. Next Steps

1. **Phase 1**: Domain models + Protobuf definitions ✅ (In Progress)
2. **Phase 2**: WAL implementation + State cache
3. **Phase 3**: gRPC service implementations
4. **Phase 4**: Adapter integrations (MT5 feeder, LP gateways)
5. **Phase 5**: ETL pipeline + Reporting plugins
6. **Phase 6**: Observability (metrics, tracing, logging)
7. **Phase 7**: Load testing + optimization
