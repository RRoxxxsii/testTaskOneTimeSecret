from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column

from src.infrastructure.sqlalchemy.models.base import AbstractModel


class SecretORM(AbstractModel):
    """
    - secret: secret data from a user
    - secret_key: key to reveal the secret
    - code: code phrase to reveal the secret
    - is_active: whether or not the secret is active
    after one usage supposed to expire
    """
    __tablename__ = "secrets"

    secret: Mapped[str] = mapped_column(String(130))
    secret_key: Mapped[str] = mapped_column(String(130))
    code: Mapped[str]
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
