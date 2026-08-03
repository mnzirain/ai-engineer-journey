from fastapi.testclient import TestClient
from app import app

client = TestClient(app)


def test_unknown_tool():

    response = client.post(
        "/mcp/invoke",
        json={
            "tool": "unknown",
            "input": {}
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["tool"] == "unknown"

    assert data["status"] == "success"

    assert "Unknown" in data["output"]["message"]


def test_session_created():

    response = client.post(
        "/mcp/invoke",
        json={
            "tool": "search",
            "input": {
                "query": "AI"
            }
        }
    )

    data = response.json()

    assert "session_id" in data

    assert len(data["session_id"]) > 10


def test_protocol_metadata():

    response = client.post(
        "/mcp/invoke",
        json={
            "tool": "search",
            "input": {
                "query": "AI"
            }
        }
    )

    data = response.json()

    assert data["metadata"]["protocol"] == "MCP"

    assert data["metadata"]["version"] == "1.0"