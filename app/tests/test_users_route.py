from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from .. import crud, oauth2, schemas
from ..database import Base, get_db
from ..main import app

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


app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

email = "test_2@example.com"


def test_create_user_success():
    response = client.post(
        "/users/",
        json={
            "email": email,
            "password": "test_password",
        },
    )

    assert response.status_code == 201, response.text

    data = response.json()
    assert data["email"] == email

    db = next(override_get_db())
    user = crud.get_user_by_email(db, email)
    assert oauth2.verify_password("test_password", user.hashed_password)


def test_create_user_fail():
    db = next(override_get_db())

    crud.create_user(
        db,
        schemas.UserCreate(
            email=email + "a",
            password="test_password",
        ),
    )

    response = client.post(
        "/users/",
        json={
            "email": email + "a",
            "password": "test_password",
        },
    )

    assert response.status_code == 400, response.text
