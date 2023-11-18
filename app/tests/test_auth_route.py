from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from .. import crud, schemas
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


email = "test@example.com"
password = "test_password"


def test_token_success():
    response = client.post(
        "/users/",
        json={
            "email": email,
            "password": password,
        },
    )
    assert response.status_code == 200, response.text

    response = client.post(
        "/auth/token", data={"username": email, "password": password}
    )

    assert response.status_code == 200, response.text


def test_token_wrong_password():
    response = client.post(
        "/auth/token", data={"username": email, "password": password + "a"}
    )

    assert response.status_code == 401, response.text
