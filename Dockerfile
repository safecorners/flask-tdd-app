FROM python:3.9-slim-buster

ARG UID=1000
ARG GID=1000

RUN groupadd -g "${GID}" python \
    && useradd --create-home --no-log-init -u "${UID}" -g "${GID}" python

# USER python
ENV POETRY_VIRTUALENVS_CREATE=FALSE
RUN pip install poetry
COPY pyproject.toml poetry.lock ./
RUN poetry install --no-root --no-dev

COPY . .
RUN poetry install

ENV PYTHONUNBUFFERED=1 PYTHONPATH=src

CMD ["poetry", "run", "gunicorn", "-w", "4", "--bind","0.0.0.0:5000", "application.wsgi:app"]