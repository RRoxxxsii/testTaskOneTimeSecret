from fastapi import FastAPI

from src.infrastructure.sqlalchemy.config import get_config
from src.infrastructure.sqlalchemy.main import build_sessions, create_engine
from src.presentation.api.di.adapters import get_uow
from src.presentation.api.di.providers import DBProvider


def init_dependencies(app: FastAPI):
    db_config = get_config()
    async_engine = create_engine(database_url=db_config.dsn)
    async_session_maker = build_sessions(async_engine)

    db = DBProvider(async_session_maker)

    app.dependency_overrides[get_uow] = db.provide_db
