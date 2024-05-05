from fastapi import Depends

from src.domain.protocols.hasher import ProtocolHasher
from src.domain.services.secret import SecretService
from src.infrastructure.sqlalchemy.uow import ABCSQLAlchemyUnitOfWork
from src.presentation.api.di.adapters import get_uow, get_hasher


def get_secret_service(
        uow: ABCSQLAlchemyUnitOfWork = Depends(get_uow),
        hasher: ProtocolHasher = Depends(get_hasher)
) -> SecretService:
    return SecretService(uow, hasher)
