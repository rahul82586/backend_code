from typing import List, Optional, Any
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from core.domains.oms.entities.deal import Deal
from core.ports.interfaces import IDealRepository
from ..mappers import deal_to_db, db_to_deal
from ..db_models import DealModel


class SqlDealRepository(IDealRepository[Deal]):
    """PostgreSQL / SQLAlchemy implementation of IDealRepository."""

    def __init__(self, session_factory=None):
        self.session_factory = session_factory

    async def save(self, deal: Deal, session: Optional[AsyncSession] = None) -> Deal:
        """
        Persists an immutable deal entity.
        If an active AsyncSession is provided (e.g. inside UnitOfWork), uses it directly.
        Otherwise, manages its own session via session_factory.
        """
        model = deal_to_db(deal)
        if session is not None:
            await session.merge(model)
            return deal

        if self.session_factory is None:
            raise ValueError("SqlDealRepository requires session or session_factory")

        async with self.session_factory() as sess:
            await sess.merge(model)
            await sess.commit()
            return deal

    async def find_by_id(self, deal_id: str, session: Optional[AsyncSession] = None) -> Optional[Deal]:
        if session is not None:
            result = await session.execute(
                select(DealModel).where(DealModel.deal_id == deal_id)
            )
            model = result.scalar_one_or_none()
            return db_to_deal(model) if model else None

        if self.session_factory is None:
            return None

        async with self.session_factory() as sess:
            result = await sess.execute(
                select(DealModel).where(DealModel.deal_id == deal_id)
            )
            model = result.scalar_one_or_none()
            return db_to_deal(model) if model else None

    async def find_by_order_id(self, order_id: str, session: Optional[AsyncSession] = None) -> List[Deal]:
        if session is not None:
            result = await session.execute(
                select(DealModel).where(DealModel.order_id == order_id)
            )
            models = result.scalars().all()
            return [db_to_deal(m) for m in models]

        if self.session_factory is None:
            return []

        async with self.session_factory() as sess:
            result = await sess.execute(
                select(DealModel).where(DealModel.order_id == order_id)
            )
            models = result.scalars().all()
            return [db_to_deal(m) for m in models]

    async def find_by_account(self, account_login: str, session: Optional[AsyncSession] = None) -> List[Deal]:
        if session is not None:
            result = await session.execute(
                select(DealModel).where(DealModel.account_login == account_login)
            )
            models = result.scalars().all()
            return [db_to_deal(m) for m in models]

        if self.session_factory is None:
            return []

        async with self.session_factory() as sess:
            result = await sess.execute(
                select(DealModel).where(DealModel.account_login == account_login)
            )
            models = result.scalars().all()
            return [db_to_deal(m) for m in models]
