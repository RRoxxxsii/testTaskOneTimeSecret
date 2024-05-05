from pydantic.main import BaseModel


class CreateSecret(BaseModel):
    secret: str
    code: str


class RevealSecret(BaseModel):
    code: str
