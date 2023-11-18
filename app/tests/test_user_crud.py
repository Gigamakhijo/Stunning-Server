from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool
import pytest

from ..crud import user
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
    db = override_get_db()

    body = {"email": email, "password": password}
    response = user.create_user(db, body)

    assert response.email == email


def test_get_user(email, password):
    db = override_get_db()

    response = user.get_user(db, email)

    assert response.email == email
