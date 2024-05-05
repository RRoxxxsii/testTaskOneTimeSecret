import secrets

from fastapi import status
from httpx import AsyncClient


async def test_generate_secret(api_client: AsyncClient):
    """
    Testing secret generation when everything is okay.
    Secret is supposed to be successfully created.
    """
    url = "/generate/"
    response = await api_client.post(
        url, json={
            "secret": "SUPER SECRET DATA",
            "code": "code",
        }
    )
    assert response.status_code == status.HTTP_201_CREATED
    assert isinstance(response.json().get("secret_key"), str)


async def test_get_secret_by_code_and_key(
        api_client: AsyncClient, create_secret_in_db, secret_data
):
    """
    Test getting secret by code and secret key when everything is okay.
    Secret is supposed to be successfully retrieved.
    """
    data = secret_data(
        code="code",
        secret_key=secrets.token_urlsafe(16),
        secret="SUPER SECRET DATA!!!"
    )
    secret = await create_secret_in_db(**data)

    url = f"/secrets/{secret.secret_key}/"
    response = await api_client.post(url, json={"code": secret.code})

    assert response.status_code == status.HTTP_200_OK


async def test_get_secret_that_already_taken(api_client: AsyncClient, create_secret_in_db, secret_data):
    """
    Test trying to get secret for the second time.
    Secret is not supposed to be retrieved from db as deleted,
    thus secret not found.
    """
    data = secret_data(
        code="code",
        secret_key=secrets.token_urlsafe(16),
        secret="SUPER SECRET DATA!!!"
    )
    secret = await create_secret_in_db(**data)

    url = f"/secrets/{secret.secret_key}/"
    await api_client.post(url, json={"code": secret.code})
    response = await api_client.post(url, json={"code": secret.code})
    assert response.status_code == status.HTTP_404_NOT_FOUND


async def test_get_secret_by_code(
        api_client: AsyncClient, create_secret_in_db, secret_data
):
    """
    Test getting secret by code and secret key when secret key is invalid.
    """
    data = secret_data(
        code="code",
        secret_key=secrets.token_urlsafe(16),
        secret="SUPER SECRET DATA!!!"
    )
    secret = await create_secret_in_db(**data)

    invalid_secret_key = "invalid_key"
    url = f"/secrets/{invalid_secret_key}/"
    response = await api_client.post(url, json={"code": secret.code})

    assert response.status_code == status.HTTP_404_NOT_FOUND


async def test_get_secret_by_key(
        api_client: AsyncClient, create_secret_in_db, secret_data
):
    """
    Test getting secret by key and code when code is invalid.
    """
    data = secret_data(
        code="code",
        secret_key=secrets.token_urlsafe(16),
        secret="SUPER SECRET DATA!!!"
    )
    secret = await create_secret_in_db(**data)

    url = f"/secrets/{secret.secret_key}/"
    response = await api_client.post(url, json={"code": "invalid_code"})

    assert response.status_code == status.HTTP_404_NOT_FOUND
