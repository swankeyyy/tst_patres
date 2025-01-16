import pytest_asyncio

from app.main import app

from fastapi.testclient import TestClient


@pytest_asyncio.fixture(scope="session", autouse=False)
def client():
    """fixture for client testing"""
    with TestClient(app) as client:
        yield client
    client.close()
