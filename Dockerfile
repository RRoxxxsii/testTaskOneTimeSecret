FROM python:3.7-alpine

WORKDIR /backend

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update && apk add python3-dev \
                          gcc \
                          libc-dev \
                          libffi-dev

COPY requirements.txt .

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . /backend

CMD alembic upgrade head && python -m src.presentation.api.main
