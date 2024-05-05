from typing import AsyncIterator

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from src.infrastructure.sqlalchemy.uow import (
    ABCSQLAlchemyUnitOfWork,
    UnitOfWork,
)


class DBProvider:
    def __init__(self, pool: async_sessionmaker[AsyncSession]):
        self.pool = pool

    async def provide_db(self) -> AsyncIterator[ABCSQLAlchemyUnitOfWork]:
        async with self.pool() as session:
            yield UnitOfWork(session)
