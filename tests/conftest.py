import copy

import pytest
from fastapi.testclient import TestClient

from src.app import activities, app


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture(autouse=True)
def reset_activities_state():
    """Restore the in-memory activities store after each test."""
    original = copy.deepcopy(activities)
    yield
    activities.clear()
    activities.update(original)
