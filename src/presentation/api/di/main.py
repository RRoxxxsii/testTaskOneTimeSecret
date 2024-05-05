from fastapi import FastAPI

from src.infrastructure.sqlalchemy.main import create_engine, build_sessions
from src.infrastructure.sqlalchemy.config import get_config
from src.presentation.api.di.adapters import get_uow, get_hasher
from src.presentation.api.di.providers import DBProvider, HasherProvider


def init_dependencies(app: FastAPI):
    db_config = get_config()
    async_engine = create_engine(database_url=db_config.dsn)
    async_session_maker = build_sessions(async_engine)

    db = DBProvider(async_session_maker)

    app.dependency_overrides[get_uow] = db.provide_db
    app.dependency_overrides[get_hasher] = HasherProvider.provide_hash
