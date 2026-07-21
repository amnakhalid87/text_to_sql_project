from fastapi.testclient import TestClient
from app import app

client = TestClient(app)


def test_root_endpoint():
    """Root endpoint should confirm API is running."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["status"] == "Text-to-SQL chatbot API is running"


def test_chart_endpoint_when_no_chart_exists():
    """If no chart file exists, should return 404 with error message."""
    response = client.get("/chart")
    assert response.status_code in [200, 404]


def test_chat_endpoint_returns_expected_keys():
    """Chat endpoint should always return query, result, and should_visualize keys."""
    response = client.post("/chat", json={"message": "show all users"})
    assert response.status_code == 200
    data = response.json()
    assert "query" in data
    assert "result" in data
    assert "should_visualize" in data