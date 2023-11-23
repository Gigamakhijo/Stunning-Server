def test_get_todos_success(authorized_client, test_todos):
    date_time = test_todos[0].date
    date = date_time.date()

    response = authorized_client.get(
        "/todos/",
        params={"date": date, "skip": 2, "limit": 4},
    )

    assert response.status_code == 200, response.text
    data = response.json()

    assert len(data) == 2


def test_get_todos_fail(client, test_todos):
    date_time = test_todos[0].date
    date = date_time.date()

    response = client.get(
        "/todos/",
        params={"date": date, "skip": 0, "limit": 100},
    )

    assert response.status_code == 401, response.text
