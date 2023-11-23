import datetime

from .. import crud, schemas


def test_add_todo(session, test_user):
    date = datetime.datetime(2023, 11, 23, 17, 24, 10)

    todo_data = {
        "dat": date,
        "icon": "iconname",
        "title": "title_",
        "contents": "content_",
        "color": "#FFFFFF",
        "done": False,
        "user_id": test_user["id"],
    }

    print(date)

    response = crud.create_todo(
        session,
        schemas.TodoCreate(
            date=date,
            icon="iconname",
            title="title_",
            contents="content_",
            color="#FFFFFF",
            done=False,
            user_id=test_user["id"],
        ),
    )

    assert response.icon == "iconname"


def test_get_todos(session, test_user, todos):
    response = crud.get_todos_by_date(
        session,
        date=datetime.date(
            2023,
        ),
        skip=1,
        limit=3,
    )

    assert response[0].date == date
    assert response[0].icon == "iconname"
    assert response[0].title == "title_"
