import datetime

from .. import crud, schemas


def test_create_todo(session):
    todo_create = schemas.TodoCreate(
        user_id=1,
        date=datetime.datetime(2023, 11, 24, 1, 45),
        icon="iconname",
        title="title_",
        contents="content_",
        color="#FFFFFF",
        done=False,
    )

    todo = crud.create_todo(session, todo_create)

    for k in ["user_id", "icon", "title", "contents", "color", "done"]:
        assert getattr(todo, k) == getattr(todo_create, k)


def test_get_todolist(session, test_todos):
    date = test_todos[0].date

    response = crud.get_todos_by_date(session,user_id=1, date=date, skip=0, limit=2)

    for val, exp in zip(response, test_todos):
        for k in ["user_id", "icon", "title", "contents", "color", "done"]:
            assert getattr(val, k) == getattr(exp, k), k


def test_modify_todo(session,test_todo):
    todo = test_todo

    todo_create = schemas.TodoCreate(
        user_id=1,
        date=datetime.datetime(2023, 11, 24, 1, 45),
        icon="iconname",
        title="title_",
        contents="content_",
        color="#FFFFFF",
        done=False,
    )

    crud.modify_todo(session,todo_id=todo.id,todo=todo_create)

    for k in ["user_id", "icon", "title", "contents", "color", "done"]:
        assert getattr(todo, k) == getattr(todo_create, k)


def test_delete_todo(session,test_todo):
    todo = test_todo

    for k in ["user_id", "icon", "title", "contents", "color", "done"]:
        assert getattr(todo, k) == getattr(test_todo, k)

    crud.delete_todo(session,todo_id=todo.id)

    response = crud.get_todo_by_todo_id(session,todo_id=todo.id)

    assert response is None





    