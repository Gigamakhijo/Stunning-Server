from .. import crud, schemas

email = "test_3@example.com"


def test_get_todos_success(authorized_client, test_todos):
    breakpoint()
    date_time = test_todos[0].date
    date = date_time.date()

    response = authorized_client.get(
        "/todos/",
        params={"date": date, "skip": 0, "limit": 100},
    )

    assert response.status_code == 200, response.text


def test_create_user_fail():
    crud.create_user(
        db,
        schemas.UserCreate(
            email=email + "a",
            password="test_password",
        ),
    )

    response = client.post(
        "/users/",
        json={
            "email": email + "a",
            "password": "test_password",
        },
    )

    assert response.status_code == 400, response.text
