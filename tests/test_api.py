import os
import pytest
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_root_endpoint():

    response = client.get("/")
    assert response.status_code == 200
    
    data = response.json()
    assert data == {"status": "Text-to-SQL chatbot API is running"}


def test_chat_endpoint_valid_payload():

    payload = {"message": "Show all users from database"}
    response = client.post("/chat", json=payload)
    
    assert response.status_code == 200
    
    data = response.json()
    assert "query" in data
    assert "result" in data
    assert "should_visualize" in data


def test_chart_endpoint_not_found():

    response = client.get("/chart")
    
    if response.status_code == 404:
        data = response.json()
        assert data == {"error": "No chart available yet"}
    else:
        assert response.status_code == 200
