from sqlalchemy.ext.asyncio import AsyncSession

from src.domain.protocols.uow import ProtocolUnitOfWork
from src.infrastructure.sqlalchemy.repositories import SecretRepository


class SecretHolder:
    def __init__(self, session: AsyncSession):
        self.secret_repo = SecretRepository(session)


class ABCSQLAlchemyUnitOfWork(ProtocolUnitOfWork):
    def __init__(self, session: AsyncSession):  # noqa
        self._session = session
        self.secret_holder = SecretHolder(session)

    async def commit(self):
        raise NotImplementedError

    async def rollback(self):
        raise NotImplementedError


class UnitOfWork(ABCSQLAlchemyUnitOfWork):

    async def commit(self):
        await self._session.commit()

    async def rollback(self):
        await self._session.rollback()
