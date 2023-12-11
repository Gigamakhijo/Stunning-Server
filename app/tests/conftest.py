import datetime
import tempfile
import uuid

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from .. import crud, oauth2, schemas, utils
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


@pytest.fixture
def session():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


@pytest.fixture
def client(session):
    def override_get_db():
        try:
            yield session
        finally:
            session.close()

    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)


@pytest.fixture
def email():
    return "test@example.com"


@pytest.fixture
def password():
    return "fakepassword"


@pytest.fixture
def profile_image():
    with tempfile.NamedTemporaryFile(mode="w+b") as jpg:
        jpg.write(b"Hello World!")

        jpg.seek(0)

        yield jpg


@pytest.fixture
def test_user(client, email, password, profile_image):
    body = {"email": email, "password": password, "username": "testuser"}

    response = client.post("/users/", json=body)
    assert response.status_code == 201, response.text
    data = response.json()
    assert data["email"] == body["email"]
    data["username"] = "testuser"

    response = client.post(
        "/users/profile_image", files={"profile_image": profile_image}
    )

    return data


@pytest.fixture
def other_test_user(client, email, password):
    email = "2" + email
    password = "2" + password

    body = {"email": email, "password": password, "username": "testuser1"}

    response = client.post("/users/", json=body)
    assert response.status_code == 201, response.text
    data = response.json()
    assert data["email"] == body["email"]
    data["password"] = body["password"]
    data["username"] = "testuser1"

    return data


@pytest.fixture
def authenticated_user(client, test_user):
    response = client.post(
        "/auth/token",
        data={"email": test_user["email"], "password": test_user["password"]},
    )

    assert response.status_code == 201, response.text


@pytest.fixture
def test_todos(test_user, session):
    todos = []
    for t in range(10):
        todo = crud.create_todo(
            session,
            schemas.TodoCreate(
                date=datetime.datetime(2023, 11, 23, t, 24, 10),
                icon="iconname",
                title=f"title_{t}",
                contents=f"content_{t}",
                color="#FFFFFF",
                done=False,
            ),
            user_id=test_user["id"],
        )

        todos.append(todo)

    return todos


@pytest.fixture
def token(test_user):
    return oauth2.create_access_token({"sub": test_user["email"]})


@pytest.fixture
def authorized_client(session, token):
    def override_get_db():
        try:
            yield session
        finally:
            session.close()

    app.dependency_overrides[get_db] = override_get_db
    client = TestClient(app)

    client.headers = {**client.headers, "Authorization": f"Bearer {token}"}

    yield client


@pytest.fixture
def test_todo(authorized_client):
    response = authorized_client.post(
        "/todos/",
        json={
            "date": str(datetime.datetime(2023, 11, 23, 1, 24, 10)),
            "icon": "iconname",
            "title": "title",
            "contents": "content",
            "color": "#FFFFFF",
            "done": False,
        },
    )

    assert response.status_code == 200, response.text

    data = response.json()

    return data


@pytest.fixture
def timestamp():
    return utils.random_date().isoformat()


@pytest.fixture
def video_url():
    return f"{uuid.uuid4()}.mp4"


@pytest.fixture
def thumbnail_url():
    return f"{uuid.uuid4()}.jpeg"


@pytest.fixture
def test_feeds(session, test_user):
    feeds = []
    for _ in range(10):
        data = {
            "timestamp": utils.random_date().isoformat(),
            "video_url": f"{uuid.uuid4()}.mp4",
            "thumbnail_url": f"{uuid.uuid4()}.jpeg",
        }

        feed = crud.create_feed(
            session,
            schemas.FeedCreate(**data),
            user_id=test_user["id"],
        )

        feeds.append({"id": feed.id, **data})

    return feeds


@pytest.fixture
def test_feed(session, test_user):
    data = {
        "timestamp": utils.random_date().isoformat(),
        "video_url": f"{uuid.uuid4()}.mp4",
        "thumbnail_url": f"{uuid.uuid4()}.jpeg",
    }

    feed = crud.create_feed(
        session,
        schemas.FeedCreate(**data),
        user_id=test_user["id"],
    )

    return {"id": feed.id, **data}


@pytest.fixture
def other_test_feeds(session, other_test_user):
    feeds = []
    for _ in range(10):
        data = {
            "timestamp": utils.random_date().isoformat(),
            "video_url": f"{uuid.uuid4()}.mp4",
            "thumbnail_url": f"{uuid.uuid4()}.jpeg",
        }

        feed = crud.create_feed(
            session,
            schemas.FeedCreate(**data),
            user_id=other_test_user["id"],
        )

        feeds.append({"id": feed.id, **data})

    return feeds


@pytest.fixture
def other_test_feed(session, other_test_user):
    data = {
        "timestamp": utils.random_date().isoformat(),
        "video_url": f"{uuid.uuid4()}.mp4",
        "thumbnail_url": f"{uuid.uuid4()}.jpeg",
    }

    feed = crud.create_feed(
        session,
        schemas.FeedCreate(**data),
        user_id=other_test_user["id"],
    )

    return {"id": feed.id, **data}
