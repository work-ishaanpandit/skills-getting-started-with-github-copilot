def test_get_activities_returns_activity_catalog(client):
    response = client.get("/activities")

    assert response.status_code == 200

    activities = response.json()
    assert isinstance(activities, dict)
    assert "Chess Club" in activities
    assert "Programming Class" in activities

    chess_club = activities["Chess Club"]
    assert chess_club["description"]
    assert chess_club["schedule"]
    assert isinstance(chess_club["max_participants"], int)
    assert isinstance(chess_club["participants"], list)