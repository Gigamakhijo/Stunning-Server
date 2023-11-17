from fastapi.testclient import TestClient
from ..routers import auth
from ..main import app

import random


def mock_create_user():
    return {"email": "leewoorim@naver.com", "hashed_password": "leewoorim"}


def mock_read_user():
    return {"email": "leewoorim@naver.com", "hashed_password": "leewoorim"}


app.dependency_overrides[auth.register_user] = mock_create_user
app.dependency_overrides[auth.get_user] = mock_read_user

client = TestClient(app)


def test_create_user_success():
    response = client.post(
        "/users/",
        json={"email": "leewoorim@naver.com", "hashed_password": "leewoorim"},
    )


# assert response.status_code == 200, response.text

# data = response.json()
# assert data["email"] == "leewoorim@naver.com"


def test_create_user_failed():
    response = client.post(
        "/users/",
        json={"email": "leewoorim@naver.com", "hashed_password": "leewoorim"},
    )
    assert response.status_code == 400, response.text


def test_get_user_success():
    user_id = 1
    response = client.get(f"/users/{user_id}")

    assert response.status_code == 200

    data = response.json()
    assert data["email"] == "leewoorim@naver.com"

    ...


def test_get_user_failed():
    user_id = random.randint(1, 10000)
    response = client.get(f"/users/{user_id}")

    assert response.status_code == 404

    ...
