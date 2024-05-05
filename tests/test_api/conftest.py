import pytest
import pytest_asyncio
from sqlalchemy.orm import sessionmaker

from src.infrastructure.sqlalchemy.models import SecretORM


@pytest.fixture
def secret_data():
    def wrapper(code: str, secret: str, secret_key: str):
        return {
            "secret": secret,
            "code": code,
            "secret_key": secret_key
        }
    return wrapper


@pytest_asyncio.fixture(scope="function")
async def create_secret_in_db(db_session_test: sessionmaker):
    async def wrapper(**kwargs):
        async with db_session_test() as session:
            secret = SecretORM(**kwargs)
            session.add(secret)
            await session.commit()
            await session.refresh(secret)
            return secret
    return wrapper

