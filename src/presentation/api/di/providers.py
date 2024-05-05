from typing import Type

from typing_extensions import AsyncIterator

from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession

from src.infrastructure.hasher.passlib import PasslibHasher
from src.infrastructure.sqlalchemy.uow import UnitOfWork, ABCSQLAlchemyUnitOfWork


class DBProvider:
    def __init__(self, pool: async_sessionmaker[AsyncSession]):
        self.pool = pool

    async def provide_db(self) -> AsyncIterator[ABCSQLAlchemyUnitOfWork]:
        async with self.pool() as session:
            yield UnitOfWork(session)


class HasherProvider:

    @staticmethod
    async def provide_hash() -> Type[PasslibHasher]:
        return PasslibHasher
