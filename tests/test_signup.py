def test_signup_adds_participant_and_rejects_duplicates(client):
    activity_name = "Chess Club"
    email = "New.Student@mergington.edu"

    first_response = client.post(
        f"/activities/{activity_name}/signup",
        params={"email": email},
    )

    assert first_response.status_code == 200
    assert first_response.json() == {
        "message": f"Signed up {email.strip().lower()} for {activity_name}"
    }

    activities = client.get("/activities").json()
    assert email.strip().lower() in activities[activity_name]["participants"]

    duplicate_response = client.post(
        f"/activities/{activity_name}/signup",
        params={"email": email.upper()},
    )

    assert duplicate_response.status_code == 400
    assert duplicate_response.json()["detail"] == "Student already signed up"


def test_signup_unknown_activity_returns_404(client):
    response = client.post(
        "/activities/Unknown Club/signup",
        params={"email": "student@mergington.edu"},
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"