import pytest

import application.imperative_models
from application.app import create_app
from application.imperative_database import db_session, engine


@pytest.fixture(scope="session")
def app():
    app = create_app()
    app.config.update(
        {
            "TESTING": True,
        }
    )

    app_context = app.app_context()
    app_context.push()

    yield app

    app_context.pop()


@pytest.fixture(scope="session")
def client(app):
    with app.test_client() as client:
        yield client
