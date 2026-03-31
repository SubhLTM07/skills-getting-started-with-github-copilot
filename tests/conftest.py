import pytest
import copy
from fastapi.testclient import TestClient
from src import app


@pytest.fixture
def client():
    """TestClient for the FastAPI app."""
    return TestClient(app.app)


@pytest.fixture(autouse=True)
def reset_activities():
    """Reset the in-memory activities database before and after each test."""
    original_activities = copy.deepcopy(app.activities)
    yield
    app.activities = original_activities


@pytest.fixture
def sample_activity():
    """Sample activity data for testing."""
    return {
        "name": "Test Club",
        "description": "A test activity",
        "schedule": "Test Time",
        "max_participants": 10,
        "participants": ["test@example.com"]
    }