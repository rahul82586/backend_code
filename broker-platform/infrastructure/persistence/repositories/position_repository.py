from typing import List, Optional
from sqlalchemy import select
from core.domains.oms.entities.position import Position
from core.ports.interfaces import IPositionRepository
from ..mappers import position_to_db, db_to_position
from ..db_models import PositionModel

class SqlPositionRepository(IPositionRepository):
    """PostgreSQL implementation of IPositionRepository."""
    
    def __init__(self, session_factory):
        self.session_factory = session_factory
    
    async def get_open_positions(self) -> List[Position]:
        async with self.session_factory() as session:
            result = await session.execute(
                select(PositionModel).where(PositionModel.volume > 0)
            )
            models = result.scalars().all()
            return [db_to_position(m) for m in models]
    
    async def get_positions_by_account(self, account_login: str) -> List[Position]:
        async with self.session_factory() as session:
            result = await session.execute(
                select(PositionModel).where(PositionModel.account_login == account_login)
            )
            models = result.scalars().all()
            return [db_to_position(m) for m in models]
    
    async def save(self, position: Position) -> Position:
        async with self.session_factory() as session:
            model = position_to_db(position)
            await session.merge(model)
            await session.commit()
            return position
    
    async def find_by_id(self, position_id: str) -> Optional[Position]:
        async with self.session_factory() as session:
            result = await session.execute(
                select(PositionModel).where(PositionModel.id == position_id)
            )
            model = result.scalar_one_or_none()
            if not model:
                return None
            return db_to_position(model)
