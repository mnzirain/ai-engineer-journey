from fastapi.testclient import TestClient
from app import app

client = TestClient(app)


def test_tool_discovery():

    response = client.get("/mcp/tools")

    assert response.status_code == 200

    data = response.json()

    assert "search" in data

    assert "summarize" in data

    assert "translate" in data


def test_search_tool():

    response = client.post(
        "/mcp/invoke",
        json={
            "tool": "search",
            "input": {
                "query": "What is Artificial Intelligence?"
            }
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["tool"] == "search"

    assert data["status"] == "success"


def test_summarize_tool():

    response = client.post(
        "/mcp/invoke",
        json={
            "tool": "summarize",
            "input": {
                "text": "Artificial Intelligence enables computers to perform tasks that normally require human intelligence."
            }
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["tool"] == "summarize"

    assert data["status"] == "success"


def test_translate_tool():

    response = client.post(
        "/mcp/invoke",
        json={
            "tool": "translate",
            "input": {
                "text": "Artificial Intelligence"
            }
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["tool"] == "translate"

    assert data["status"] == "success"