from copy import deepcopy

import pytest
from fastapi.testclient import TestClient

from src.app import activities, app


@pytest.fixture()
def client():
    original_activities = deepcopy(activities)

    # Arrange: ensure each test starts from a clean in-memory state.
    activities.clear()
    activities.update(deepcopy(original_activities))

    with TestClient(app) as test_client:
        yield test_client

    # Assert-style cleanup: restore baseline data for the next test.
    activities.clear()
    activities.update(original_activities)
