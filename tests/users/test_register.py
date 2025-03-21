import pytest
from typing import Dict
from app.core.api_response import APIResponse

def test_register_user_success(client, mock_user_service):
    """Test successful user registration."""

    # Send request
    response_duplicate =client.post("v1/users/register", json={
        "first_name": "Alice",
        "last_name": "Smith",
        "email": "alice@example111.com",
        "password": "SecurePass123"
    })
    json_data=response_duplicate.json()
    # Assertions for duplicate user
    assert json_data["status_code"]==400
    assert json_data['status'] is False
    # Assertions for successfull user registration
    response =client.post("v1/users/register", json={
        "first_name": "Alice",
        "last_name": "Smith",
        "email": "alice@example1112111.com",
        "password": "SecurePass123"
    })
    json_data_success=response.json()
    assert json_data_success["status_code"] == 201
    assert json_data_success["status"] is True
    assert "data" in json_data_success
