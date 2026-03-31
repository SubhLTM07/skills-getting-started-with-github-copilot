"""Tests for GET /activities and GET / endpoints."""


def test_get_activities_success(client):
    """Test GET /activities returns all activities."""
    # Arrange
    expected_activities = [
        "Chess Club", "Programming Class", "Gym Class", "Basketball Team",
        "Tennis Club", "Drama Club", "Art Studio", "Debate Team", "Science Club"
    ]

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert len(data) == 9
    assert all(activity in data for activity in expected_activities)
    # Check structure of one activity
    chess_club = data["Chess Club"]
    assert "description" in chess_club
    assert "schedule" in chess_club
    assert "max_participants" in chess_club
    assert "participants" in chess_club
    assert isinstance(chess_club["participants"], list)


def test_get_root_redirect(client):
    """Test GET / redirects to static frontend."""
    # Arrange
    # No special setup needed

    # Act
    response = client.get("/", follow_redirects=False)

    # Assert
    assert response.status_code == 307
    assert response.headers["location"] == "/static/index.html"