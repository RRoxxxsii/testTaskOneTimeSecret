import uvicorn
from fastapi import FastAPI

from src.presentation.api.di.main import init_dependencies
from src.presentation.api.routers import init_routers


def build_app() -> FastAPI:
    app = FastAPI()
    init_dependencies(app)
    init_routers(app)
    return app


if __name__ == "__main__":
    uvicorn.run(
        app="src.presentation.api.main:build_app",
        host="0.0.0.0",
        port=8000,
        reload=True,
    )
