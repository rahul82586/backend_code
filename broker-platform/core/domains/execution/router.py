"""
Smart Order Router (SOR).

This module implements the logic to evaluate an approved Order against
active RoutingRules and determine the execution destination.

Architectural Purpose:
Decouples the decision logic (WHERE to send) from the execution logic (HOW to send).
Allows dynamic reconfiguration of routing rules without changing core code.
"""
from typing import List, Optional
from decimal import Decimal
import logging
import fnmatch

from core.domains.execution.models import (
    RoutingRule, 
    ExecutionInstruction, 
    ExecutionDestination
)
from core.domains.oms.entities.order import Order
from core.domains.accounts.models import Account
from core.ports.interfaces import IRoutingRuleRepository

logger = logging.getLogger(__name__)


class SmartOrderRouter:
    """
    Evaluates an approved Order against active RoutingRules.
    Returns an ExecutionInstruction telling the orchestrator where to send it.
    
    Rules are evaluated by priority (highest first). First match wins.
    If no rule matches, falls back to a server default (configurable).
    
    Supports dynamic rule reloading via IRoutingRuleRepository.
    """
    
    def __init__(
        self, 
        routing_rule_repo: IRoutingRuleRepository,
        default_destination: ExecutionDestination = ExecutionDestination.B_BOOK
    ):
        self.repo = routing_rule_repo
        self.default_destination = default_destination
        self.rules: List[RoutingRule] = []
        logger.info("SmartOrderRouter initialized with dynamic rule loading")
    
    async def refresh_rules(self):
        """Reload routing rules from repository. Call this on startup and periodically."""
        self.rules = await self.repo.get_active_rules()
        self.rules = sorted(self.rules, key=lambda r: r.priority, reverse=True)
        logger.info(f"SmartOrderRouter loaded {len(self.rules)} active rules")

    def route(self, order: Order, account: Account) -> ExecutionInstruction:
        """
        Evaluate rules and return where this order should go.
        
        Args:
            order: The approved order to route.
            account: The account owning the order (for Group checks).
            
        Returns:
            ExecutionInstruction with destination and metadata.
        """
        if not self.rules:
            # Auto-refresh if rules haven't been loaded yet
            raise RuntimeError("Routing rules not loaded. Call refresh_rules() first.")
        
        logger.debug(f"Routing order {order.ticket_id} for account {account.login_id}")
        
        for rule in self.rules:
            if not rule.is_enabled:
                continue
                
            if self._matches(rule, order, account):
                logger.info(
                    f"Order {order.ticket_id} matched rule '{rule.rule_id}' "
                    f"-> Destination: {rule.destination.value}"
                )
                return ExecutionInstruction(
                    destination=rule.destination,
                    rule_id=rule.rule_id,
                    gateway_id=rule.gateway_id,
                    coverage_account_id=rule.coverage_account_id,
                    reason=f"Matched rule: {rule.rule_id}"
                )
        
        # Fallback to default
        logger.warning(
            f"No routing rule matched for order {order.ticket_id}. "
            f"Using default: {self.default_destination.value}"
        )
        return ExecutionInstruction(
            destination=self.default_destination,
            rule_id="DEFAULT_FALLBACK",
            reason="No matching rule found"
        )

    def _matches(self, rule: RoutingRule, order: Order, account: Account) -> bool:
        """
        Check if order/account matches all rule filters.
        
        Returns True only if ALL specified filters match.
        None filters are ignored (wildcard).
        Supports MT5-style wildcards like 'real_*' and 'EUR*' using fnmatch.
        """
        # 1. Group Filter (supports wildcards)
        if rule.group_filter is not None:
            if not fnmatch.fnmatch(account.group.name, rule.group_filter):
                return False
        
        # 2. Symbol Filter (supports wildcards)
        if rule.symbol_filter is not None:
            if not fnmatch.fnmatch(order.symbol, rule.symbol_filter):
                return False
        
        # 3. Volume Min Filter
        if rule.volume_min is not None:
            if order.volume.value < rule.volume_min:
                return False
        
        # 4. Volume Max Filter
        if rule.volume_max is not None:
            if order.volume.value > rule.volume_max:
                return False
        
        return True
