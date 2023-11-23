from .. import crud, oauth2


def test_create_user_success(client, session, email, password):
    body = {"email": email, "password": password}

    response = client.post(
        "/users/",
        json=body,
    )

    assert response.status_code == 201, response.text

    data = response.json()
    assert data["email"] == email

    user = crud.get_user_by_email(session, email)
    assert oauth2.verify_password(password, user.hashed_password)


def test_create_user_fail(client, test_user):
    response = client.post(
        "/users/",
        json={
            "email": test_user["email"],
            "password": "asdf",
        },
    )

    assert response.status_code == 400, response.text
