def test_get_follows_success(authorized_client):
    response = authorized_client.get("/follows/", params={"skip": 2, "limit": 4})

    assert response.status_code == 200, response.text
    data = response.json()


def test_get_follows_fail(client):
    response = client.get("/follows/", params={"skip": 2, "limit": 4})

    assert response.status_code == 401, response.text
    data = response.json()


def test_add_follow_success(authorized_client):
    response = authorized_client.post("/follows/", json={"followee_id": 1})

    assert response.status_code == 200, response.text


def test_add_follow_failed(client):
    response = client.post("/follows/", json={"followee_id": 1})

    assert response.status_code == 401, response.text
