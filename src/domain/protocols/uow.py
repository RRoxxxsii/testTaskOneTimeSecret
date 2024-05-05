from typing_extensions import Protocol


class ProtocolUnitOfWork(Protocol):
    """
    Protocol class for unit of work pattern
    Supposed to be inherited and implemented
    """

    def __init__(self):
        raise NotImplementedError

    async def commit(self):
        raise NotImplementedError

    async def rollback(self):
        raise NotImplementedError
