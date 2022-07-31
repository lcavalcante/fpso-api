FROM python:3.10-slim-bullseye

RUN apt-get update
RUN apt-get install -y curl
RUN curl -sSL https://install.python-poetry.org | python -

COPY app /app
COPY poetry.lock pyproject.toml /
RUN /root/.local/bin/poetry install

ENTRYPOINT ["/root/.local/bin/poetry", "run"]
CMD ["uvicorn", "app.main:app"]


