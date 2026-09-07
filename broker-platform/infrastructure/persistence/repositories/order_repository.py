from typing import List, Optional
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from core.domains.oms.entities.order import Order, OrderState
from core.ports.interfaces import IOrderRepository
from ..mappers import order_to_db, db_to_order
from ..db_models import OrderModel

class SqlOrderRepository(IOrderRepository):
    """PostgreSQL implementation of IOrderRepository."""
    
    def __init__(self, session_factory):
        self.session_factory = session_factory
    
    async def save(self, order: Order) -> Order:
        async with self.session_factory() as session:
            model = order_to_db(order)
            await session.merge(model)
            await session.commit()
            return order
    
    async def find_by_id(self, order_id: str) -> Optional[Order]:
        async with self.session_factory() as session:
            result = await session.execute(
                select(OrderModel).where(OrderModel.ticket_id == order_id)
            )
            model = result.scalar_one_or_none()
            if not model:
                return None
            return db_to_order(model)
    
    async def find_active_orders_by_account(self, account_login: str) -> List[Order]:
        async with self.session_factory() as session:
            active_states = [s.value for s in [OrderState.NEW, OrderState.PLACED, OrderState.PARTIALLY_FILLED]]
            result = await session.execute(
                select(OrderModel).where(
                    OrderModel.account_login == account_login,
                    OrderModel.state.in_(active_states)
                )
            )
            models = result.scalars().all()
            return [db_to_order(m) for m in models]
    
    async def get_next_ticket_id(self) -> str:
        # Simplified - in production use a sequence
        import uuid
        return f"ORD_{uuid.uuid4().hex[:12]}"
