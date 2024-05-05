# One time secret service - Test Task

-----

## Run Locally

Clone the project:

```bash
  git clone https://github.com/RRoxxxsii/testTaskOneTimeSecret.git
```

Copy `.env.example` to `.env`:

```bash
cp .env.example .env
```

Run with docker-compose:
```bash
docker compose up --build
```

Run tests:
```bash
docker exec -it secret-backend pytest
```

-----

## Available endpoints:

**POST /generate/**

*accepts secret and code phrase and returns secret key
to reveal the secret later*

```bash
curl -X "POST" \
  "http://localhost:8000/generate/" \
  -d '{
    "secret": "YOUR_SECRET_DATA",
    "code": "secret_code"
}' -H "Content-Type: application/json"
```
```{"secret_key":"Eb0Kt5bJhAYXy1VUqSBVBA"}```
``STATUS 201``

**POST /secrets/< yourSecretKeyGoesHere >**

*requires secret key as a path param and code in body to reveal
your secret data, if already revealed or not found returns 404*
```bash
curl -X "POST" \
  "http://localhost:8000/secrets/<PLACE YOUR SECRET KEY>/"  \
  -d '{
    "code": "secret_code"
  }' -H "Content-Type: application/json"
```
```{"secret":"YOUR_SECRET_DATA"}```
```STATUS 200```

```{"detail":"Not found secret"}```
```STATUS 404```

----
## Main dependencies

**PYTHON 3.7**

### Infrastructure

* PostgreSQL
* Docker

### Python libs

* FastAPI
* Pydantic
* Alembic
* asyncpg
* SQLAlchemy
* pytest
* pytest_asyncio
