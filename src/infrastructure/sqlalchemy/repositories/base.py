from abc import ABC, abstractmethod
from typing import Generic, Iterable, Optional, Type, TypeVar

from sqlalchemy import delete, select, update
from sqlalchemy.ext.asyncio import AsyncSession

from src.infrastructure.sqlalchemy.models.base import AbstractModel

Model = TypeVar("Model", bound=AbstractModel)


class AbstractRepository(Generic[Model], ABC):
    def __init__(self, session: AsyncSession, model: Type[Model]):
        self._session = session
        self.model = model

    @abstractmethod
    async def create(self, **kwargs) -> Model:
        raise NotImplementedError

    @abstractmethod
    async def get_by_id(self, id_: int) -> Optional[Model]:
        raise NotImplementedError

    @abstractmethod
    async def get_all(self) -> Iterable[Model]:
        raise NotImplementedError

    @abstractmethod
    async def update_obj(self, id_: int, **kwargs) -> None:
        raise NotImplementedError

    @abstractmethod
    async def delete_obj(self, id_: int) -> None:
        raise NotImplementedError


class BaseRepository(AbstractRepository[Model]):
    async def create(self, **kwargs) -> Model:
        """Creates an instance of a model"""
        obj = self.model(**kwargs)
        self._session.add(obj)
        await self._session.commit()
        await self._session.refresh(obj)
        return obj

    async def get_by_id(self, id_: int) -> Optional[Model]:
        """Selects and returns an instance of a model by id"""
        stmt = select(self.model).where(self.model.id == id_)
        return (await self._session.execute(stmt)).scalar_one_or_none()

    async def get_all(self) -> Iterable[Model]:
        """Selects and returns all instances of a model"""
        result = await self._session.execute(select(self.model))
        return result.scalars().all()

    async def update_obj(self, id_: int, **kwargs) -> None:
        """Updates and object by id"""
        query = update(self.model).where(self.model.id == id_).values(kwargs)
        await self._session.execute(query)

    async def delete_obj(self, id_: int) -> None:
        """Deletes and object by id"""
        query = delete(self.model).where(self.model.id == id_)
        await self._session.execute(query)
