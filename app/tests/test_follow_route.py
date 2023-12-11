def test_follow(authorized_client, other_test_user):
    response = authorized_client.post(
        f"/follows/{other_test_user['id']}",
    )

    assert response.status_code == 201, response.text


def test_unfollow(authorized_client, other_test_user):
    response = authorized_client.post(
        f"/follows/{other_test_user['id']}",
    )

    assert response.status_code == 201, response.text

    response = authorized_client.delete(
        f"/follows/{other_test_user['id']}",
    )

    assert response.status_code == 204, response.text


def test_follower_list(authorized_client, client, test_user, other_test_user):
    response = client.post(
        "/auth/token",
        data={
            "username": other_test_user["email"],
            "password": other_test_user["password"],
        },
    )

    assert response.status_code == 200, response.text
    token = response.json()["access_token"]

    response = authorized_client.post(
        f"/follows/{other_test_user['id']}",
    )

    assert response.status_code == 201, response.text

    response = client.post(
        f"/follows/{test_user['id']}",
        headers={"Authorization": f"Bearer {token}"},
    )

    assert response.status_code == 201, response.text

    response = authorized_client.get("/follows/")
    assert response.status_code == 200, response.text
    data = response.json()
    print(data)

    assert len(data) == 1
