import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import pytest
from unittest.mock import AsyncMock, MagicMock
from fastapi.testclient import TestClient
from app.main import app
from app.services.user_service import UserService

@pytest.fixture
def mock_user_service():
    """
    Create a mock for UserService
    """
    mock_service=AsyncMock(spec=UserService)
    return mock_service
@pytest.fixture
def client(mock_user_service):
    """
    Override DI for testing
    """
    app.dependency_overrides[UserService]=lambda: mock_user_service
    with TestClient(app) as client:
        yield client
    app.dependency_overrides.clear()