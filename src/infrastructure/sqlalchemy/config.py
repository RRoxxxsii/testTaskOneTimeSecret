import os
from dataclasses import dataclass


@dataclass(frozen=True)
class DBConfig:
    port: str = os.getenv("POSTGRES_PORT")
    user: str = os.getenv("POSTGRES_USER")
    password: str = os.getenv("POSTGRES_PASSWORD")
    host: str = os.getenv("POSTGRES_HOST")
    db_name: str = os.getenv("POSTGRES_DB")

    @property
    def dsn(self) -> str:
        return (
            f"postgresql+asyncpg://"
            f"{self.user}:"
            f"{self.password}"
            f"@{self.host}:{self.port}/"
            f"{self.db_name}"
        )


def get_config() -> DBConfig:
    return DBConfig()
