# 🏛️ Institutional Brokerage Backend Platform

Production-grade, MetaTrader 5-equivalent distributed trading backend with Protobuf/gRPC contracts, Hot/Cold storage split, and institutional features.

## Architecture Overview

This platform implements a **language-agnostic** microservices architecture with:

- **Protocol-first design**: Strict Protobuf/gRPC contracts between services
- **Hot/Cold storage split**: In-memory state + WAL for zero-latency trading path
- **MT5/Centroid compatibility**: Native support for A/B-book routing, Risk Accounts, EMIR/NFA reporting
- **Plugin architecture**: Swappable components (Python → Rust/C++) via dependency injection

## Directory Structure

```
broker_platform/
├── protocol/              # Protobuf definitions & generated stubs
├── domain/                # Pure business logic (no I/O)
├── core_engine/           # Hot path: matching, positions, WAL, state cache
├── services/              # Long-running microservices
├── adapters/              # External I/O boundaries (MT5 feeds, LP gateways)
├── plugins/               # Regulatory reporting plugins
├── storage/               # Hot/Cold/Warehouse data layers
├── observability/         # Metrics, tracing, logging
├── deploy/                # Docker, K8s, secrets
└── tests/                 # Unit, integration, load tests
```

## Getting Started

### Prerequisites
- Python 3.10+
- Protocol Buffers compiler (`protoc`)
- Docker & Docker Compose
- Redis (for state cache)
- PostgreSQL (for warehouse/cold storage ETL)

### Quick Start (Development)

```bash
# Install dependencies
pip install -r requirements.txt

# Generate protobuf stubs
make proto-generate

# Run local development stack
docker-compose -f deploy/compose/dev.yml up -d

# Run tests
pytest tests/unit
```

## Key Components

| Component | Responsibility |
|-----------|----------------|
| **Access Service** | Auth, JWT, rate limiting, DDoS protection |
| **OMS Service** | Order lifecycle, dealer queue, state machine |
| **Risk Service** | Async margin checks, stop-outs, NOP limits |
| **Matching Service** | TOB/CLOB execution engine |
| **History Service** | Tick ingestion, OHLCV aggregation, news parsing |

## Documentation

- [Architecture Master Plan](docs/architecture.md)
- [Protocol Specifications](protocol/README.md)
- [API Reference](docs/api.md)
- [Deployment Guide](deploy/README.md)

## License

Proprietary - All rights reserved
