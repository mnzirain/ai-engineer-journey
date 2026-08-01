from fastapi.testclient import TestClient
from app import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert "Week 16" in data["message"]


def test_list_tools():
    response = client.get("/tools")
    assert response.status_code == 200

    data = response.json()

    assert "available_tools" in data

    tool_names = [tool["name"] for tool in data["available_tools"]]

    assert "search" in tool_names
    assert "summarize" in tool_names
    assert "translate" in tool_names


def test_search_tool():
    response = client.post(
        "/tool",
        json={"query": "What is Retrieval-Augmented Generation?"}
    )

    assert response.status_code == 200

    data = response.json()

    assert data["tool"] == "search"
    assert data["status"] == "success"


def test_summarize_tool():
    response = client.post(
        "/tool",
        json={"query": "Summarize Artificial Intelligence"}
    )

    assert response.status_code == 200

    data = response.json()

    assert data["tool"] == "summarize"
    assert data["status"] == "success"


def test_translate_tool():
    response = client.post(
        "/tool",
        json={"query": "Translate Artificial Intelligence into French"}
    )

    assert response.status_code == 200

    data = response.json()

    assert data["tool"] == "translate"
    assert data["status"] == "success"