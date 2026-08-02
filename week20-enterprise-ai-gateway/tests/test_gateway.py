from fastapi.testclient import TestClient

from app import app

client = TestClient(app)


def test_root():

    response = client.get("/")

    assert response.status_code == 200

    data = response.json()

    assert data["status"] == "running"


def test_health():

    response = client.get("/health")

    assert response.status_code == 200

    data = response.json()

    assert data["status"] == "healthy"


def test_providers():

    response = client.get("/providers")

    assert response.status_code == 200


def test_models():

    response = client.get("/models")

    assert response.status_code == 200


def test_generate():

    response = client.post(
        "/generate",
        headers={
            "api-key": "gateway-admin"
        },
        json={
            "provider": "OpenAI",
            "model": "GPT-4",
            "prompt": "Hello"
        }
    )

    assert response.status_code == 200


def test_metrics():

    response = client.get("/metrics")

    assert response.status_code == 200