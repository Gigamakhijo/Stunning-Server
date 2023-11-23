from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from .. import crud, schemas
from ..database import Base
import datetime

SQLALCHEMY_DATABASE_URL = "sqlite://"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base.metadata.create_all(bind=engine)

def test_create_todo(session):
    db = session

    response = crud.create_todo(
        db,
        schemas.TodoCreate(
            user_id=1,
            date= datetime.datetime(2023,11,24,1,45),
            icon="iconname",
            title="title_",
            contents="content_",
            color="#FFFFFF",
            done=False,
        ),
    )

    assert response.icon == "iconname"


def test_get_todolist(session):
    db = session

    response = crud.create_todo(
        db,
        schemas.TodoCreate(
            user_id=1,
            date= datetime.datetime(2023,11,24,1,45),
            icon="iconname",
            title="title_",
            contents="content_",
            color="#FFFFFF",
            done=False,
        ),
    )
    
    crud.create_todo(
        db,
        schemas.TodoCreate(
            user_id=1,
            date=datetime.datetime(2023,11,25,1,45),
            icon="iconname",
            title="title",
            contents="content",
            color="#FFFFFF",
            done=False,
        ),
    )

    date = response.date

    response = crud.get_todos_by_date(db, date=date)

    assert len(response) == 1
    assert response[0].date == date
    assert response[0].icon == "iconname"
    assert response[0].title == "title_"


    ...
