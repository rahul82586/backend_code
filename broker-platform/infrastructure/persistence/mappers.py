from core.domains.accounts.models import Account, Group, AccountType
from core.domains.oms.entities.order import Order, OrderState, OrderType
from core.domains.oms.entities.deal import Deal, DealType
from core.domains.oms.entities.position import Position
from core.domains.instruments.models import Symbol
from core.domains.ledger.models import BalanceOperation, BalanceOperationType
from core.domains.execution.models import RoutingRule, CoverageAccount, ExecutionDestination
from core.domains.common.value_objects import Money, Price, Volume
from decimal import Decimal
import json

from infrastructure.persistence.db_models import (
    AccountModel, GroupModel, SymbolModel, OrderModel, 
    DealModel, PositionModel, BalanceOperationModel,
    RoutingRuleModel, CoverageAccountModel
)


# Account Mappers
def account_to_db(account: Account) -> AccountModel:
    """Convert domain Account to database model."""
    return AccountModel(
        login=account.login_id,
        group_name=account.group.name,
        account_type=account.account_type.value,
        balance=account.balance.amount,
        equity=account.equity.amount,
        margin_used=account.margin_used.amount,
        margin_free=account.margin_free.amount,
        is_enabled=account.is_enabled,
        kyc_verified=account.kyc_verified,
        currency=account.balance.currency
    )


def db_to_account(model: AccountModel, group: Group) -> Account:
    """Convert database model to domain Account."""
    account = Account(
        login_id=model.login,
        group=group,
        account_type=AccountType(model.account_type),
        balance=Money(model.balance, model.currency)
    )
    account.equity = Money(model.equity, model.currency)
    account.margin_used = Money(model.margin_used, model.currency)
    account.margin_free = Money(model.margin_free, model.currency)
    account.is_enabled = model.is_enabled
    account.kyc_verified = model.kyc_verified
    return account


# Group Mappers
def group_to_db(group: Group) -> GroupModel:
    """Convert domain Group to database model."""
    return GroupModel(
        name=group.name,
        leverage=group.margin.leverage,
        margin_call_level=group.margin.margin_call_level,
        stop_out_level=group.margin.stop_out_level,
        stop_out_mode=group.margin.stop_out_mode,
        commission_type=group.commission.type,
        commission_value=group.commission.value,
        commission_currency=group.commission.currency,
        execution_mode=group.execution.mode.value,
        position_mode="HEDGING" if group.execution.allow_hedging else "NETTING",
        allow_hedging=group.execution.allow_hedging,
        allow_scalping=group.execution.allow_scalping,
        slippage_points=group.execution.slippage_points,
        permissions_json=json.dumps(group.permissions),
        swap_enable=True,
        swap_long=Decimal('0'),
        swap_short=Decimal('0')
    )


def db_to_group(model: GroupModel) -> Group:
    """Convert database model to domain Group."""
    from core.domains.accounts.models import MarginProfile, CommissionProfile, ExecutionProfile
    
    margin_profile = MarginProfile(
        leverage=model.leverage,
        margin_call_level=model.margin_call_level,
        stop_out_level=model.stop_out_level,
        stop_out_mode=model.stop_out_mode
    )
    
    commission_profile = CommissionProfile(
        type=model.commission_type,
        value=model.commission_value,
        currency=model.commission_currency
    )
    
    execution_profile = ExecutionProfile(
        mode=ExecutionMode(model.execution_mode),
        allow_hedging=model.allow_hedging,
        allow_scalping=model.allow_scalping,
        slippage_points=model.slippage_points
    )
    
    return Group(
        name=model.name,
        margin=margin_profile,
        commission=commission_profile,
        execution=execution_profile,
        permissions=json.loads(model.permissions_json or "{}")
    )


# Order Mappers
def order_to_db(order: Order) -> OrderModel:
    return OrderModel(
        ticket_id=order.ticket_id,
        account_login=order.account_login,
        symbol=order.symbol,
        order_type=order.order_type.value,
        volume=order.volume.value,
        filled_volume=order.filled_volume.value,
        price=order.price.value if order.price else None,
        average_fill_price=order.average_fill_price.value if order.average_fill_price else None,
        stop_loss=order.stop_loss.value if order.stop_loss else None,
        take_profit=order.take_profit.value if order.take_profit else None,
        state=order.state.value
    )


def db_to_order(model: OrderModel) -> Order:
    return Order(
        ticket_id=model.ticket_id,
        account_login=model.account_login,
        symbol=model.symbol,
        order_type=OrderType(model.order_type),
        volume=Volume(model.volume),
        price=Price(model.price) if model.price else None,
        stop_loss=Price(model.stop_loss) if model.stop_loss else None,
        take_profit=Price(model.take_profit) if model.take_profit else None,
        state=OrderState(model.state),
        filled_volume=Volume(model.filled_volume),
        average_fill_price=Price(model.average_fill_price) if model.average_fill_price else None
    )


# Deal Mappers
def deal_to_db(deal: Deal, currency: str = "USD") -> DealModel:
    return DealModel(
        deal_id=deal.deal_id,
        order_id=deal.order_id,
        account_login=deal.account_login,
        symbol=deal.symbol,
        deal_type=deal.deal_type.value,
        volume=deal.volume.value,
        price=deal.price.value,
        commission=deal.commission.amount,
        swap=deal.swap.amount,
        profit=deal.profit.amount,
        currency=currency,
        original_deal_id=deal.original_deal_id,
        reason=deal.reason
    )


def db_to_deal(model: DealModel) -> Deal:
    return Deal(
        deal_id=model.deal_id,
        order_id=model.order_id,
        account_login=model.account_login,
        symbol=model.symbol,
        deal_type=DealType(model.deal_type),
        volume=Volume(model.volume),
        price=Price(model.price),
        commission=Money(model.commission, model.currency),
        swap=Money(model.swap, model.currency),
        profit=Money(model.profit, model.currency),
        original_deal_id=model.original_deal_id,
        reason=model.reason
    )


# Position Mappers
def position_to_db(position: Position) -> PositionModel:
    return PositionModel(
        id=position.id,
        account_login=position.account_login,
        symbol=position.symbol,
        volume=position.volume.value,
        side=position.side.value,
        average_price=position.average_price.value,
        unrealized_pnl=position.unrealized_pnl.amount,
        swap_accumulated=position.swap_accumulated.amount,
        contract_size=position.contract_size
    )


def db_to_position(model: PositionModel) -> Position:
    return Position(
        id=model.id,
        account_login=model.account_login,
        symbol=model.symbol,
        volume=Volume(model.volume),
        side=OrderType.BUY if model.side == "BUY" else OrderType.SELL,
        average_price=Price(model.average_price),
        unrealized_pnl=Money(model.unrealized_pnl, "USD"),
        swap_accumulated=Money(model.swap_accumulated, "USD"),
        contract_size=model.contract_size
    )


# Symbol Mappers
def symbol_to_db(symbol: Symbol) -> SymbolModel:
    sessions_list = [{"start": s.start.isoformat(), "end": s.end.isoformat(), "day": s.day_of_week} for s in symbol.sessions]
    return SymbolModel(
        name=symbol.name,
        path=symbol.path,
        tick_size=symbol.tick_size,
        tick_value=symbol.tick_value,
        contract_size=symbol.contract_size,
        digits=symbol.digits,
        volume_min=symbol.volume_min,
        volume_max=symbol.volume_max,
        volume_step=symbol.volume_step,
        margin_initial_percent=symbol.margin_initial_percent,
        margin_maintenance_percent=symbol.margin_maintenance_percent,
        is_trade_allowed=symbol.is_trade_allowed,
        fill_mode=symbol.fill_mode,
        sessions_json=json.dumps(sessions_list)
    )


def db_to_symbol(model: SymbolModel) -> Symbol:
    from datetime import time
    sessions_data = json.loads(model.sessions_json or "[]")
    sessions = []
    for s in sessions_data:
        sessions.append(None)  # Simplified - would need proper time parsing
    
    return Symbol(
        name=model.name,
        path=model.path,
        tick_size=model.tick_size,
        tick_value=model.tick_value,
        contract_size=model.contract_size,
        digits=model.digits,
        volume_min=model.volume_min,
        volume_max=model.volume_max,
        volume_step=model.volume_step,
        margin_initial_percent=model.margin_initial_percent,
        margin_maintenance_percent=model.margin_maintenance_percent,
        is_trade_allowed=model.is_trade_allowed,
        fill_mode=model.fill_mode,
        sessions=sessions
    )


# BalanceOperation Mappers
def balance_operation_to_db(operation: BalanceOperation) -> BalanceOperationModel:
    return BalanceOperationModel(
        operation_id=operation.operation_id,
        account_login=operation.account_login,
        operation_type=operation.operation_type.value,
        amount=operation.amount.amount,
        currency=operation.amount.currency,
        balance_after=operation.balance_after.amount,
        reference_id=operation.reference_id,
        comment=operation.comment
    )


def db_to_balance_operation(model: BalanceOperationModel) -> BalanceOperation:
    return BalanceOperation(
        operation_id=model.operation_id,
        account_login=model.account_login,
        operation_type=BalanceOperationType(model.operation_type),
        amount=Money(model.amount, model.currency),
        balance_after=Money(model.balance_after, model.currency),
        reference_id=model.reference_id,
        comment=model.comment,
        created_at=model.created_at
    )


# RoutingRule Mappers
def routing_rule_to_db(rule: RoutingRule) -> RoutingRuleModel:
    return RoutingRuleModel(
        rule_id=rule.rule_id,
        priority=rule.priority,
        destination=rule.destination.value,
        group_filter=rule.group_filter,
        symbol_filter=rule.symbol_filter,
        volume_min=rule.volume_min,
        volume_max=rule.volume_max,
        gateway_id=rule.gateway_id,
        coverage_account_id=rule.coverage_account_id,
        is_enabled=rule.is_enabled
    )


def db_to_routing_rule(model: RoutingRuleModel) -> RoutingRule:
    return RoutingRule(
        rule_id=model.rule_id,
        priority=model.priority,
        destination=ExecutionDestination(model.destination),
        group_filter=model.group_filter,
        symbol_filter=model.symbol_filter,
        volume_min=model.volume_min,
        volume_max=model.volume_max,
        gateway_id=model.gateway_id,
        coverage_account_id=model.coverage_account_id,
        is_enabled=model.is_enabled
    )


# CoverageAccount Mappers
def coverage_account_to_db(account: CoverageAccount) -> CoverageAccountModel:
    return CoverageAccountModel(
        account_id=account.account_id,
        name=account.name,
        currency=account.currency,
        net_exposure_json=json.dumps({k: str(v) for k, v in account.net_exposure.items()}),
        margin_level=account.margin_level,
        trading_state=account.trading_state
    )


def db_to_coverage_account(model: CoverageAccountModel) -> CoverageAccount:
    net_exposure_dict = json.loads(model.net_exposure_json or "{}")
    net_exposure = {k: Decimal(v) for k, v in net_exposure_dict.items()}
    
    return CoverageAccount(
        account_id=model.account_id,
        name=model.name,
        currency=model.currency,
        net_exposure=net_exposure,
        margin_level=model.margin_level,
        trading_state=model.trading_state
    )
