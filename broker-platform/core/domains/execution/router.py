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

from core.domains.execution.models import (
    RoutingRule, 
    ExecutionInstruction, 
    ExecutionDestination
)
from core.domains.oms.entities.order import Order
from core.domains.accounts.models import Account

logger = logging.getLogger(__name__)


class SmartOrderRouter:
    """
    Evaluates an approved Order against active RoutingRules.
    Returns an ExecutionInstruction telling the orchestrator where to send it.
    
    Rules are evaluated by priority (highest first). First match wins.
    If no rule matches, falls back to a server default (configurable).
    """
    
    def __init__(
        self, 
        rules: List[RoutingRule], 
        default_destination: ExecutionDestination = ExecutionDestination.B_BOOK
    ):
        # Sort rules by priority descending (highest first)
        self.rules = sorted(rules, key=lambda r: r.priority, reverse=True)
        self.default_destination = default_destination
        logger.info(f"SmartOrderRouter initialized with {len(rules)} rules")

    def route(self, order: Order, account: Account) -> ExecutionInstruction:
        """
        Evaluate rules and return where this order should go.
        
        Args:
            order: The approved order to route.
            account: The account owning the order (for Group checks).
            
        Returns:
            ExecutionInstruction with destination and metadata.
        """
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
                    reason=f"Matched rule: {rule.rule_id}"
                )
        
        # Fallback to default
        logger.warning(
            f"No routing rule matched for order {order.ticket_id}. "
            f"Using default: {self.default_destination.value}"
        )
        return ExecutionInstruction(
            destination=self.default_destination,
            rule_id="DEFAULT",
            reason="No matching rule found"
        )

    def _matches(self, rule: RoutingRule, order: Order, account: Account) -> bool:
        """
        Check if order/account matches all rule filters.
        
        Returns True only if ALL specified filters match.
        None filters are ignored (wildcard).
        """
        # 1. Group Filter
        if rule.group_filter is not None:
            if account.group.name != rule.group_filter:
                return False
        
        # 2. Symbol Filter
        if rule.symbol_filter is not None:
            if order.symbol != rule.symbol_filter:
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
