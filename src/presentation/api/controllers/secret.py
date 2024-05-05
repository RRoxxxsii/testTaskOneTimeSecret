from typing import Union

from fastapi import APIRouter, Depends, Response, status

from src.domain.dto.secret import CreateSecretDTO, RevealSecretDTO
from src.domain.exceptions.secret import SecretNotFound
from src.domain.services.secret import SecretService
from src.presentation.api.controllers.request import CreateSecret, RevealSecret
from src.presentation.api.controllers.response import (
    NotFoundSecretResponse,
    SecretKeyResponse,
    SecretResponse,
)
from src.presentation.api.di.services import get_secret_service

router = APIRouter(tags=["Secret"])


@router.post("/generate/", status_code=status.HTTP_201_CREATED)
async def generate_secret(
    schema: CreateSecret, service: SecretService = Depends(get_secret_service)
) -> SecretKeyResponse:
    secret_key = await service.create(CreateSecretDTO(**schema.dict()))
    return SecretKeyResponse(secret_key=secret_key)


@router.post("/secrets/{secret_key}/", status_code=status.HTTP_200_OK)
async def get_secret_by_key(
    secret_key: str,
    schema: RevealSecret,
    response: Response,
    service: SecretService = Depends(get_secret_service),
) -> Union[SecretResponse, NotFoundSecretResponse]:
    dto = RevealSecretDTO(secret_key=secret_key, code=schema.code)
    try:
        secret = await service.get_secret(dto)
    except SecretNotFound:
        response.status_code = status.HTTP_404_NOT_FOUND
        return NotFoundSecretResponse()
    else:
        return SecretResponse(secret=secret)
