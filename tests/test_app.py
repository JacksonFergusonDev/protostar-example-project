"""Tests for the orbit-api service."""

from fastapi.testclient import TestClient

from orbit_api.app import app

client = TestClient(app)


def test_health() -> None:
    """The health endpoint answers."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
