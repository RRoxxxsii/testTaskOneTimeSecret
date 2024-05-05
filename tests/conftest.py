import asyncio
from typing import Any, AsyncGenerator, Generator

import pytest
import pytest_asyncio
from fastapi import FastAPI
from httpx import AsyncClient
from sqlalchemy import text
from sqlalchemy.orm import close_all_sessions, sessionmaker

from src.infrastructure.sqlalchemy.config import get_config
from src.infrastructure.sqlalchemy.main import build_sessions, create_engine
from src.presentation.api.di.main import init_dependencies
from src.presentation.api.routers import init_routers


def build_testapp() -> FastAPI:
    """Creating FastAPI application for testing purposes"""
    app = FastAPI()
    init_routers(app)
    init_dependencies(app)
    return app


@pytest_asyncio.fixture(scope="session")
async def db_session_test() -> sessionmaker:
    yield build_sessions(create_engine(get_config().dsn))
    close_all_sessions()


@pytest.fixture(scope="session")
def event_loop() -> Generator:
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest_asyncio.fixture(scope="function", autouse=True)
async def clean_tables(db_session_test) -> None:
    tables = ("secrets",)
    async with db_session_test() as session:
        for table in tables:
            statement = text(f"""TRUNCATE TABLE {table} CASCADE;""")
            await session.execute(statement)
            await session.commit()


@pytest_asyncio.fixture(scope="function")
async def api_client() -> AsyncGenerator[AsyncClient, Any]:
    async with AsyncClient(
        app=build_testapp(), base_url="http://test"
    ) as client_:
        yield client_
