import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from .. import crud, oauth2, schemas
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


@pytest.fixture
def email():
    return "test@example.com"


@pytest.fixture
def password():
    return "fakepassword"


def test_create_user(email, password):
    db = next(override_get_db())

    response = crud.create_user(
        db,
        schemas.UserCreate(
            email="hi",
            hashed_password=password + "fake_hash",
        ),
    )

    assert response.email == "hi"
    assert response.hashed_password == password + "fake_hash"


def test_get_user(email, password):
    db = next(override_get_db())

    email = email + "a"

    crud.create_user(
        db,
        schemas.UserCreate(
            email=email,
            hashed_password=password,
        ),
    )

    user = crud.get_user_by_email(db, email)

    assert user.email == email
    assert user.hashed_password == password
