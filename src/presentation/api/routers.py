from fastapi import FastAPI

from src.presentation.api.controllers.secret import router as secret_router


def init_routers(app: FastAPI):
    app.include_router(secret_router)
