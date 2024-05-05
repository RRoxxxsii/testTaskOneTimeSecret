from src.domain.protocols.hasher import ProtocolHasher
from src.infrastructure.sqlalchemy.uow import ABCSQLAlchemyUnitOfWork


class BaseService:
    """
    Base service initializer for all services and usecases
    Supposed to be inherited
    """
    def __init__(self, uow: ABCSQLAlchemyUnitOfWork, hasher: ProtocolHasher):
        self.uow = uow
        self.hasher = hasher


class BaseSecretService(BaseService):
    """
    Base secret service initializer for Secret service and usecase
    Supposed to be inherited
    """
    pass
