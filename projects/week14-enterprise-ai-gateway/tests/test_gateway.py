from fastapi.testclient import TestClient
from app import app

client = TestClient(app)


def test_home():
    response = client.get("/")
    assert response.status_code == 200


def test_health():
    response = client.get("/health")
    assert response.status_code == 200


def test_stats():
    response = client.get("/stats")
    assert response.status_code == 200


def test_search():
    response = client.post(
        "/search",
        json={"query": "What is Artificial Intelligence?"}
    )

    assert response.status_code == 200

    data = response.json()

    assert "results" in data
    assert len(data["results"]) > 0