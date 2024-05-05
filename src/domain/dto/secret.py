from dataclasses import dataclass

from src.domain.dto.base import BaseDTO


@dataclass(frozen=True)
class CreateSecretDTO(BaseDTO):
    """
    secret - secret itself
    code - code phrase to reveal the secret
    """

    secret: str
    code: str


@dataclass(frozen=True)
class RevealSecretDTO(BaseDTO):
    """
    secret key - key to secret
    code - code phrase to reveal the secret
    """

    secret_key: str
    code: str
