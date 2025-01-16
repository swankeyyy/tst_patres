import pytest


@pytest.mark.asyncio
async def test_create_user(client):
    """Test endpoint for read all products"""
    headers = {"username": "test22", "password": "<PASSWORD>"}
    response = client.post("/api/users/register", headers=headers)
    data = response.json()
    assert response.status_code == 200
    assert data["username"] == headers["username"]
