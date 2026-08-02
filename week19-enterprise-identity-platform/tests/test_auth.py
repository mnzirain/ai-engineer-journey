from fastapi.testclient import TestClient
from app import app

client = TestClient(app)


def test_login_endpoint_exists():
    response = client.post("/login", json={})
    assert response.status_code in [200, 400, 401, 422]