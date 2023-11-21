from flask import Flask, Response
import pytest

# Import the Flask app from your main module
from app import app

@pytest.fixture
def client():
    # Create a test client using the app fixture
    with app.test_client() as client:
        yield client

def test_hello_route(client):
    # Send a GET request to the "/hello" route
    response = client.get("/")

    # Check if the status code is 200 (OK)
    assert response.status_code == 200

    # Check if the response data contains "Hello World"
    assert b'Hello World' in response.data

# Add more tests as needed
