from sqlalchemy import Column, Integer, String, Numeric, DateTime, Boolean, Text, ForeignKey, Index
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.sql import func
from decimal import Decimal
import enum


class Base(DeclarativeBase):
    pass


class AccountModel(Base):
    """Database model for trading Account."""
    __tablename__ = "accounts"
    login = Column(String(32), primary_key=True)
    group_name = Column(String(128), ForeignKey("groups.name"), nullable=False)
    account_type = Column(String(32), nullable=False, default="REAL")
    balance = Column(Numeric(18, 8), nullable=False, default=0)
    credit = Column(Numeric(18, 8), nullable=False, default=0)
    equity = Column(Numeric(18, 8), nullable=False, default=0)
    margin_used = Column(Numeric(18, 8), nullable=False, default=0)
    margin_free = Column(Numeric(18, 8), nullable=False, default=0)
    leverage = Column(Integer, nullable=False, default=100)
    is_enabled = Column(Boolean, nullable=False, default=True)
    kyc_verified = Column(Boolean, nullable=False, default=False)
    currency = Column(String(3), nullable=False, default="USD")
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())


class GroupModel(Base):
    """Database model for Group (rule engine)."""
    __tablename__ = "groups"
    name = Column(String(128), primary_key=True)
    leverage = Column(Integer, nullable=False, default=100)
    margin_call_level = Column(Numeric(6, 2), nullable=False, default=60)
    stop_out_level = Column(Numeric(6, 2), nullable=False, default=30)
    stop_out_mode = Column(String(16), nullable=False, default="PERCENT")
    commission_type = Column(String(16), nullable=False, default="MONEY")
    commission_value = Column(Numeric(18, 8), nullable=False, default=0)
    commission_currency = Column(String(3), nullable=False, default="USD")
    execution_mode = Column(String(32), nullable=False, default="MARKET")
    position_mode = Column(String(16), nullable=False, default="HEDGING")
    allow_hedging = Column(Boolean, default=True)
    allow_scalping = Column(Boolean, default=True)
    slippage_points = Column(Integer, default=0)
    permissions_json = Column(Text, default="{}")
    swap_enable = Column(Boolean, default=True)
    swap_type = Column(String(16), default="POINTS")
    swap_long = Column(Numeric(18, 8), default=0)
    swap_short = Column(Numeric(18, 8), default=0)
    created_at = Column(DateTime(timezone=True), server_default=func.now())


class SymbolModel(Base):
    """Database model for tradable Symbol."""
    __tablename__ = "symbols"
    name = Column(String(32), primary_key=True)
    path = Column(String(128), nullable=False)
    tick_size = Column(Numeric(18, 8), nullable=False)
    tick_value = Column(Numeric(18, 8), nullable=False)
    contract_size = Column(Numeric(18, 8), nullable=False, default=100000)
    digits = Column(Integer, nullable=False, default=5)
    volume_min = Column(Numeric(18, 8), nullable=False, default=Decimal('0.01'))
    volume_max = Column(Numeric(18, 8), nullable=False, default=Decimal('100'))
    volume_step = Column(Numeric(18, 8), nullable=False, default=Decimal('0.01'))
    margin_initial_percent = Column(Numeric(6, 2), nullable=False, default=Decimal('3.33'))
    margin_maintenance_percent = Column(Numeric(6, 2), nullable=False, default=Decimal('1.67'))
    is_trade_allowed = Column(Boolean, nullable=False, default=True)
    fill_mode = Column(String(16), nullable=False, default="FOK")
    sessions_json = Column(Text, default="[]")
    created_at = Column(DateTime(timezone=True), server_default=func.now())


class OrderModel(Base):
    """Database model for Order (client intent)."""
    __tablename__ = "orders"
    ticket_id = Column(String(32), primary_key=True)
    account_login = Column(String(32), ForeignKey("accounts.login"), nullable=False)
    symbol = Column(String(32), ForeignKey("symbols.name"), nullable=False)
    order_type = Column(String(32), nullable=False)
    volume = Column(Numeric(18, 8), nullable=False)
    filled_volume = Column(Numeric(18, 8), nullable=False, default=0)
    price = Column(Numeric(18, 8), nullable=True)
    average_fill_price = Column(Numeric(18, 8), nullable=True)
    stop_loss = Column(Numeric(18, 8), nullable=True)
    take_profit = Column(Numeric(18, 8), nullable=True)
    state = Column(String(32), nullable=False, default="NEW")
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    __table_args__ = (
        Index("idx_orders_login", "account_login"),
        Index("idx_orders_symbol", "symbol"),
        Index("idx_orders_state", "state"),
    )


class DealModel(Base):
    """Database model for Deal (immutable execution record)."""
    __tablename__ = "deals"
    deal_id = Column(String(32), primary_key=True)
    order_id = Column(String(32), ForeignKey("orders.ticket_id"), nullable=False)
    account_login = Column(String(32), ForeignKey("accounts.login"), nullable=False)
    symbol = Column(String(32), ForeignKey("symbols.name"), nullable=False)
    deal_type = Column(String(32), nullable=False)
    volume = Column(Numeric(18, 8), nullable=False)
    price = Column(Numeric(18, 8), nullable=False)
    commission = Column(Numeric(18, 8), nullable=False, default=0)
    swap = Column(Numeric(18, 8), nullable=False, default=0)
    profit = Column(Numeric(18, 8), nullable=False, default=0)
    currency = Column(String(3), nullable=False, default="USD")
    original_deal_id = Column(String(32), nullable=True)
    reason = Column(String(256), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    __table_args__ = (
        Index("idx_deals_login", "account_login"),
        Index("idx_deals_order", "order_id"),
        Index("idx_deals_symbol", "symbol"),
    )


class PositionModel(Base):
    """Database model for Position (aggregate open state)."""
    __tablename__ = "positions"
    id = Column(String(64), primary_key=True)
    account_login = Column(String(32), ForeignKey("accounts.login"), nullable=False)
    symbol = Column(String(32), ForeignKey("symbols.name"), nullable=False)
    volume = Column(Numeric(18, 8), nullable=False)
    side = Column(String(8), nullable=False)
    average_price = Column(Numeric(18, 8), nullable=False)
    unrealized_pnl = Column(Numeric(18, 8), nullable=False, default=0)
    swap_accumulated = Column(Numeric(18, 8), nullable=False, default=0)
    contract_size = Column(Numeric(18, 8), nullable=False, default=100000)
    opened_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    __table_args__ = (
        Index("idx_positions_login", "account_login"),
        Index("idx_positions_symbol", "symbol"),
    )


class BalanceOperationModel(Base):
    """Database model for immutable BalanceOperation (ledger)."""
    __tablename__ = "balance_operations"
    operation_id = Column(String(32), primary_key=True)
    account_login = Column(String(32), ForeignKey("accounts.login"), nullable=False)
    operation_type = Column(String(32), nullable=False)
    amount = Column(Numeric(18, 8), nullable=False)
    currency = Column(String(3), nullable=False, default="USD")
    balance_after = Column(Numeric(18, 8), nullable=False)
    reference_id = Column(String(64), nullable=True)
    comment = Column(String(256), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    __table_args__ = (
        Index("idx_balance_ops_login", "account_login"),
        Index("idx_balance_ops_type", "operation_type"),
        Index("idx_balance_ops_reference", "reference_id"),
    )


class RoutingRuleModel(Base):
    """Database model for RoutingRule."""
    __tablename__ = "routing_rules"
    rule_id = Column(String(32), primary_key=True)
    priority = Column(Integer, nullable=False)
    destination = Column(String(32), nullable=False)
    group_filter = Column(String(128), nullable=True)
    symbol_filter = Column(String(64), nullable=True)
    volume_min = Column(Numeric(18, 8), nullable=True)
    volume_max = Column(Numeric(18, 8), nullable=True)
    gateway_id = Column(String(64), nullable=True)
    coverage_account_id = Column(String(64), nullable=True)
    is_enabled = Column(Boolean, nullable=False, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())


class CoverageAccountModel(Base):
    """Database model for CoverageAccount (broker risk account)."""
    __tablename__ = "coverage_accounts"
    account_id = Column(String(64), primary_key=True)
    name = Column(String(128), nullable=False)
    currency = Column(String(3), nullable=False, default="USD")
    net_exposure_json = Column(Text, default="{}")
    margin_level = Column(Numeric(18, 8), nullable=False, default=0)
    trading_state = Column(String(32), nullable=False, default="NEUTRAL")
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())


class DomainEventModel(Base):
    """Database model for event sourcing / audit trail."""
    __tablename__ = "domain_events"
    event_id = Column(String(64), primary_key=True)
    event_type = Column(String(64), nullable=False)
    aggregate_id = Column(String(64), nullable=False)
    payload_json = Column(Text, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    __table_args__ = (
        Index("idx_events_type", "event_type"),
        Index("idx_events_aggregate", "aggregate_id"),
    )
