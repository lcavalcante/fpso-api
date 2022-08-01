FROM python:3.10-slim-bullseye

RUN apt-get update
RUN apt-get install -y curl
RUN curl -sSL https://install.python-poetry.org | python -

COPY alembic.ini /
COPY poetry.lock pyproject.toml /
RUN /root/.local/bin/poetry install
COPY alembic /alembic
COPY app /app

ENTRYPOINT ["/root/.local/bin/poetry", "run"]
CMD ["uvicorn", "--host", "0.0.0.0" ,"app.main:app"]
