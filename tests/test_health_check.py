import pytest

from application.app import create_app


def test_config():
    assert not create_app().testing
    assert create_app({"TESTING": True}).testing


def test_health_check(client):
    response = client.get("/health-check/")

    assert response.status_code == 200
    assert response.json["status"] == "healthy"
