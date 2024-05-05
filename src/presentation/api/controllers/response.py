from pydantic import BaseModel, Field


class SecretKeyResponse(BaseModel):
    secret_key: str


class SecretResponse(BaseModel):
    secret: str


class NotFoundSecretResponse(BaseModel):
    detail = Field("Not found secret", const=True)
