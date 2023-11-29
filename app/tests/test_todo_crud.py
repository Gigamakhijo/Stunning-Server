import datetime

from .. import crud, schemas


def test_create_todo(session):
    todo_create = schemas.TodoCreate(
        date=datetime.datetime(2023, 11, 24, 1, 45),
        icon="iconname",
        title="title_",
        contents="content_",
        color="#FFFFFF",
        done=False,
    )

    todo = crud.create_todo(session, todo_create, user_id=1)

    for k in ["icon", "title", "contents", "color", "done"]:
        assert getattr(todo, k) == getattr(todo_create, k)


def test_get_todolist(session, test_todos):
    date = test_todos[0].date

    response = crud.get_todos_by_date(
        session, user_id=test_todos[0].user_id, date=date, skip=0, limit=2
    )

    for val, exp in zip(response, test_todos):
        for k in ["user_id", "icon", "title", "contents", "color", "done"]:
            assert getattr(val, k) == getattr(exp, k), k


def test_update_todo(session, test_todo):
    crud.update_todo(
        session, todo=schemas.TodoEdit(**test_todo), todo_id=test_todo["id"]
    )

    new_todo = crud.get_todo(session, test_todo["id"])

    for k in ["user_id", "icon", "title", "contents", "color", "done"]:
        assert getattr(new_todo, k) == test_todo[k]


def test_delete_todo(session, test_todo):
    crud.delete_todo(session, test_todo["id"])

    todo = crud.get_todo(session, test_todo["id"])

    assert todo is None
