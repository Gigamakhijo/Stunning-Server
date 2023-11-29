from .. import schemas


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
    print(data)


def test_get_todos_fail(client, test_todos):
    date_time = test_todos[0].date
    date = date_time.date()

    response = client.get("/todos/", params={"date": date, "skip": 0, "limit": 100})

    assert response.status_code == 401, response.text


def test_add_todo_success(authorized_client, test_todo: schemas.TodoCreate, test_user):
    date_time = test_todo["date"]
    date = str(date_time)

    response = authorized_client.post("/todos/", json={"date": date, **test_todo})

    assert response.status_code == 200, response.text
    data = response.json()


def test_add_todo_failed(client, test_todo: schemas.TodoCreate):
    date_time = test_todo["date"]
    date = str(date_time)

    response = client.post("/todos/", json={"date": date, **test_todo})

    assert response.status_code == 401, response.text


def test_modify_todo_success(authorized_client, test_todo):
    todo_id = 1
    date_time = test_todo["date"]
    date = str(date_time)

    authorized_client.post(
        f"/todos/{todo_id}",
        json={"date": date, **test_todo},
    )

    response = authorized_client.put(
        f"/todos/{todo_id}",
        json={"todo_id": todo_id, "date": date, **test_todo},
    )

    assert response.status_code == 200, response.text


def test_modify_todo_failed(client, test_todo):
    date_time = test_todo["date"]
    date = str(date_time)

    response = client.put(
        f"/todos/{test_todo.id}",
        json={"date": date, **test_todo},
    )

    assert response.status_code == 401, response.text


def test_delete_todo_success(authorized_client, test_todo):
    todo_id = 1
    authorized_client.delete(f"/todos/{todo_id}")

    response = authorized_client.delete(f"/todos/{todo_id}")

    assert response.status_code == 204


def test_delete_todo_failed(client):
    todo_id = 1
    response = client.delete(f"/todos/{todo_id}")

    assert response.status_code == 401
