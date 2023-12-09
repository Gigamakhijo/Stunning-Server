from .. import crud, oauth2


def test_create_user(client, session, email, password):
    body = {
        "email": email,
        "password": password,
        "full_name": "asdf",
        "gender": "asldfkjasdkf",
        "phone_number": "laksdjfalksdjf",
        "status_message": "lsadkfjalskdfj",
    }

    response = client.post("/users/", json=body)

    assert response.status_code == 201, response.text

    data = response.json()
    assert data["email"] == email

    user = crud.get_user_by_email(session, email)
    assert oauth2.verify_password(password, user.hashed_password)


def test_create_profile_image(authorized_client, profile_image):
    response = authorized_client.post(
        "/users/profile_image", files={"profile_image": profile_image}
    )
    assert response.status_code == 201, response.text


def test_update_profile_image(authorized_client, profile_image):
    response = authorized_client.post(
        "/users/profile_image", files={"profile_image": profile_image}
    )
    assert response.status_code == 201, response.text

    response = authorized_client.put(
        "/users/profile_image", files={"profile_image": profile_image}
    )
    assert response.status_code == 200, response.text


def test_create_user_fail(client, test_user):
    response = client.post(
        "/users/",
        json={"email": test_user["email"], "password": "asdf"},
    )

    assert response.status_code == 400, response.text


def test_get_current_user(authorized_client, test_user):
    response = authorized_client.get("/users/me")

    assert response.status_code == 200, response.text
    data = response.json()

    for key in test_user.keys():
        assert data[key] == test_user[key]


def test_update_user_success(authorized_client):
    response = authorized_client.put(
        "/users/me",
        json={
            "full_name": "1234",
            "username": "asdf",
        },
    )

    assert response.status_code == 200, response.text
    data = response.json()

    assert data["full_name"] == "1234"
    assert data["username"] == "asdf"
