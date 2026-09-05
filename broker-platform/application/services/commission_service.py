import logging
from decimal import Decimal
from core.domains.oms.entities.deal import Deal
from core.domains.accounts.models import Account
from core.domains.ledger.models import BalanceOperationType
from core.domains.ledger.engine import LedgerEngine
from core.domains.common.value_objects import Money
from core.ports.interfaces import IEventBus
from core.events.domain_events import DomainEvent, EventType

logger = logging.getLogger(__name__)


class CommissionService:
    """
    Calculates and applies commissions on every deal.
    Mirrors MT5 commission modes: per-lot, per-volume, percentage.
    """
    
    def __init__(self, ledger_engine: LedgerEngine, event_bus: IEventBus):
        self.ledger_engine = ledger_engine
        self.event_bus = event_bus

    async def apply_commission(self, deal: Deal, account: Account) -> Money:
        """
        Calculate commission based on account's Group commission profile.
        Deduct from account balance and record as BalanceOperation.
        Returns the commission amount (always negative for client).
        """
        commission_profile = account.group.commission
        
        # Calculate commission amount based on mode
        if commission_profile.type == "MONEY":
            # Fixed amount per deal
            commission_amount = Money(commission_profile.value, commission_profile.currency)
        elif commission_profile.type == "LOTS":
            # Per lot (e.g., $7 per 1 lot)
            commission_amount = Money(
                commission_profile.value * deal.volume.value,
                commission_profile.currency
            )
        elif commission_profile.type == "VOLUME":
            # Per volume unit (e.g., $0.00007 per unit)
            # Assuming standard lot size of 100,000 units
            commission_amount = Money(
                commission_profile.value * deal.volume.value * Decimal('100000'),
                commission_profile.currency
            )
        else:
            commission_amount = Money(Decimal('0'), "USD")
        
        # Commission is always a charge (negative for client)
        commission_charge = Money(-commission_amount.amount, commission_amount.currency)
        
        # Record in ledger
        operation = await self.ledger_engine.record_operation(
            account_login=account.login_id,
            operation_type=BalanceOperationType.COMMISSION,
            amount=commission_charge,
            reference_id=deal.deal_id,
            comment=f"Commission on deal {deal.deal_id}"
        )
        
        # Emit event
        event = DomainEvent(
            event_type=EventType.COMMISSION_CHARGED,
            aggregate_id=deal.deal_id,
            payload={
                'deal_id': deal.deal_id,
                'account_login': account.login_id,
                'commission_amount': str(commission_charge.amount),
                'currency': commission_charge.currency
            }
        )
        await self.event_bus.publish(event)
        
        logger.info(f"Commission applied: {commission_charge.amount} {commission_charge.currency} for account {account.login_id}")
        
        return commission_charge
