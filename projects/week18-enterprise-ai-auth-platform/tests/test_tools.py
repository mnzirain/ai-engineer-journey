from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

API_KEY = "doctor-key-456"


def test_search_tool():

    response = client.post(
        "/mcp",
        json={
            "api_key": API_KEY,
            "tool": "search",
            "payload": {
                "query": "Artificial Intelligence"
            }
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["status"] == "success"
    assert data["tool"] == "search"


def test_summarize_tool():

    response = client.post(
        "/mcp",
        json={
            "api_key": API_KEY,
            "tool": "summarize",
            "payload": {
                "text": "Artificial Intelligence enables computers to perform tasks normally requiring human intelligence."
            }
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["status"] == "success"
    assert data["tool"] == "summarize"


def test_translate_tool():

    response = client.post(
        "/mcp",
        json={
            "api_key": API_KEY,
            "tool": "translate",
            "payload": {
                "text": "Artificial Intelligence",
                "language": "French"
            }
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["status"] == "success"
    assert data["tool"] == "translate"