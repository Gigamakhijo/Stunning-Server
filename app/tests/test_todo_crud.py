from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from .. import crud, schemas
from ..database import Base

SQLALCHEMY_DATABASE_URL = "sqlite://"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base.metadata.create_all(bind=engine)


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


def test_add_todo():
    db = next(override_get_db())

    response = crud.add_todo(
        db,
        schemas.Todo(
            date="1",
            icon="iconname",
            title="title_",
            contents="content_",
            color="#FFFFFF",
            done=False,
        ),
    )

    assert response.icon == "iconname"


def test_get_todolist():
    db = next(override_get_db())

    response = crud.add_todo(
        db,
        schemas.Todo(
            date="1",
            icon="iconname",
            title="title_",
            contents="content_",
            color="#FFFFFF",
            done=False,
        ),
    )

    date = response.date

    response = crud.get_todolist(db, date=date)

    assert response[0].date == date
    assert response[0].icon == "iconname"
    assert response[0].title == "title_"
    ...
