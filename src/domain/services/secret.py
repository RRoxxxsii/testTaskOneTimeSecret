import secrets

from src.domain.dto.secret import CreateSecretDTO, RevealSecretDTO
from src.domain.exceptions.secret import SecretNotFound
from src.domain.services.base import BaseSecretService


class CreateSecretUseCase(BaseSecretService):
    """Secret creating use case that interacts with repository"""
    async def __call__(self, dto: CreateSecretDTO) -> str:
        secret_key = secrets.token_urlsafe(16)
        secret = await self.uow.secret_holder.secret_repo.create(
            secret_key=secret_key, **dto.dict()
        )
        await self.uow.commit()
        return secret.secret_key


class GetSecretUseCase(BaseSecretService):
    """Use case to get secret by key and code phrase"""
    async def __call__(self, dto: RevealSecretDTO) -> str:
        secret = await self.uow.secret_holder.secret_repo.get_by_key(
            secret_key=dto.secret_key, code=dto.code
        )
        if secret:
            secret_key = secret.secret_key
            await self.uow.secret_holder.secret_repo.delete_obj(secret.id)
            await self.uow.commit()

            return secret_key
        raise SecretNotFound


class SecretService(BaseSecretService):
    """Interactor that handles all use case related to secrets"""
    async def create(self, dto: CreateSecretDTO) -> str:
        return await CreateSecretUseCase(self.uow, self.hasher)(dto)

    async def get_secret(self, dto: RevealSecretDTO) -> str:
        return await GetSecretUseCase(self.uow, self.hasher)(dto)
