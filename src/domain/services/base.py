from src.infrastructure.sqlalchemy.uow import ABCSQLAlchemyUnitOfWork


class BaseService:
    """
    Base service initializer for all services and usecases
    Supposed to be inherited
    """

    def __init__(self, uow: ABCSQLAlchemyUnitOfWork):
        self.uow = uow


class BaseSecretService(BaseService):
    """
    Base secret service initializer for Secret service and usecase
    Supposed to be inherited
    """

    pass
