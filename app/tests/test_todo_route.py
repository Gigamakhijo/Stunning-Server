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


def test_get_todos_fail(client, test_todos):
    date_time = test_todos[0].date
    date = date_time.date()

    response = client.get(
        "/todos/",
        params={"date": date, "skip": 0, "limit": 100},
    )

    assert response.status_code == 401, response.text


def test_add_todo_success(authorized_client,test_todo: schemas.TodoCreate):
    date_time = test_todo.date
    date = str(date_time)

    response = authorized_client.post(
        "/todos/add",
        json = {
            "date": date,
            "icon": test_todo.icon,
            "title": test_todo.title,
            "contents": test_todo.contents,
            "color": test_todo.color,
            "done": test_todo.done,
            "user_id": test_todo.user_id,
        }
    )

    assert response.status_code == 200, response.text


def test_add_todo_failed(client,test_todo: schemas.TodoCreate):
    date_time = test_todo.date
    date = str(date_time)

    response = client.post(
        "/todos/add",
        json = {
            "date": date,
            "icon": test_todo.icon,
            "title": test_todo.title,
            "contents": test_todo.contents,
            "color": test_todo.color,
            "done": test_todo.done,
            "user_id": test_todo.user_id,
        }
    )

    assert response.status_code == 401, response.text

    ...
