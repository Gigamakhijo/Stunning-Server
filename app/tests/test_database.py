def test_create_user(client):
    response = client.post(
        "/users/",
        json={
            "id": 1,
            "email": "deadpool@example.com",
            "password": "chimichangas4life",
        },
    )
    assert response.status_code == 201, response.text
    data = response.json()
    assert data["email"] == "deadpool@example.com"
    assert "id" in data
    user_id = data["id"]

    response = client.post(
        "/auth/token",
        data={
            "username": "deadpool@example.com",
            "password": "chimichangas4life",
        },
    )
    assert response.status_code == 200, response.text
    data = response.json()

    response = client.get(
        "/users/me",
        headers={"Authorization": f"{data['token_type']} {data['access_token']}"},
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["email"] == "deadpool@example.com"
    assert data["id"] == user_id
