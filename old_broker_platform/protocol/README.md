# Protocol Definitions

This directory contains the language-agnostic Protobuf contracts that define all communication between services.

## Structure

```
protocol/
├── proto/                 # Source .proto files
│   ├── order.proto        # Order, OrderReject, OrderFill events
│   ├── tick.proto         # QuoteTick, TradeTick, OrderBookDelta
│   ├── account.proto      # AccountState, MarginCall, StopOut events
│   └── report.proto       # EMIR/NFA report generation requests
├── gen_python/            # Generated Python stubs (grpcio-tools)
└── gen_rust/              # Generated Rust stubs (prost-build)
```

## Generating Stubs

### Python
```bash
python -m grpc_tools.protoc \
  -I./proto \
  --python_out=./gen_python \
  --grpc_python_out=./gen_python \
  ./proto/*.proto
```

### Rust
```bash
prost-build --include_path=./proto --out_dir=./gen_rust ./proto/*.proto
```

## Protocol Files Overview

| File | Purpose |
|------|---------|
| `order.proto` | Order submission, modification, cancellation, fills, rejects |
| `tick.proto` | Market data: quotes, trades, order book updates |
| `account.proto` | Account state, balance updates, margin events |
| `report.proto` | Regulatory reporting requests and responses |

## Versioning

All protobuf messages should include a `version` field. Breaking changes require:
1. New message type (e.g., `OrderV2`)
2. Backward-compatible field additions only (use reserved field numbers)
3. Update service version in gRPC metadata
