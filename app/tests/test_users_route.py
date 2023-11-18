from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from .. import crud, schemas
from .. import oauth2
from ..main import app
from ..database import Base, get_db

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
hashed_password = oauth2.get_password_hash("test_password")


def test_create_user_success():
    response = client.post(
        "/users/",
        json={
            "email": email,
            "hashed_password": hashed_password,
        },
    )

    assert response.status_code == 200


def test_create_user_fail():
    db = next(override_get_db())

    crud.create_user(
        db,
        schemas.UserCreate(
            email=email + "a",
            hashed_password=hashed_password,
        ),
    )

    response = client.post(
        "/users/",
        json={
            "email": email + "a",
            "hashed_password": hashed_password,
        },
    )

    assert response.status_code == 400
