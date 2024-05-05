from fastapi import Depends

from src.domain.services.secret import SecretService
from src.infrastructure.sqlalchemy.uow import ABCSQLAlchemyUnitOfWork
from src.presentation.api.di.adapters import get_uow


def get_secret_service(
    uow: ABCSQLAlchemyUnitOfWork = Depends(get_uow),
) -> SecretService:
    return SecretService(uow)
