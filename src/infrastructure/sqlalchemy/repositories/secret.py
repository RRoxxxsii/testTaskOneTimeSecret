from abc import ABC, abstractmethod
from typing import Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.infrastructure.sqlalchemy.models import SecretORM
from src.infrastructure.sqlalchemy.repositories.base import BaseRepository, AbstractRepository


class ABCSecretRepository(AbstractRepository[SecretORM], ABC):

    @abstractmethod
    async def get_by_key(self, secret_key: str, code: str) -> Optional[SecretORM]:
        raise NotImplementedError


class SecretRepository(BaseRepository[SecretORM], ABCSecretRepository):

    def __init__(self, session: AsyncSession):
        self._session = session
        super().__init__(session, SecretORM)

    async def get_by_key(self, secret_key: str, code: str) -> Optional[SecretORM]:
        """Get secret by key and code"""
        stmt = select(self.model).where(
            self.model.secret_key == secret_key,
            self.model.code == code
        )
        res = await self._session.execute(stmt)
        return res.scalar_one_or_none()
