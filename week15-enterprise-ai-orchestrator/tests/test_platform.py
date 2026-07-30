from fastapi.testclient import TestClient
from app import app

client = TestClient(app)


def test_home():
    response = client.get("/")
    assert response.status_code == 200

    data = response.json()

    assert "message" in data
    assert "Enterprise AI Platform" in data["message"]


def test_semantic_search():

    response = client.post(
        "/ask",
        json={
            "query": "What is Retrieval-Augmented Generation?"
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["task"] == "semantic_search"
    assert len(data["results"]) > 0


def test_search_then_summarize():

    response = client.post(
        "/ask",
        json={
            "query": "Summarize Retrieval-Augmented Generation"
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["task"] == "search_then_summarize"
    assert "summary" in data


def test_search_summarize_translate():

    response = client.post(
        "/ask",
        json={
            "query": "Translate Retrieval-Augmented Generation into French"
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["task"] == "search_summarize_translate"
    assert "translation" in data