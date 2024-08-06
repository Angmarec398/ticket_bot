
ARG PYTHON_VERSION=3.9
FROM python:${PYTHON_VERSION}-slim as base

ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY pyproject.toml poetry.lock /app/

# Install Poetry
RUN pip install poetry

# Install the project dependencies using Poetry
RUN poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi

COPY . /app/

CMD ["python","bot.py"]
