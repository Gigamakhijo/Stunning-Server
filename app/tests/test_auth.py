from fastapi.testclient import TestClient
from ..routers import auth
from ..main import app
from .. import crud


def mock_create_user():
    return {"email": "leewoorim@naver.com", "hashed_password": "leewoorim"}


def mock_read_user():
    return {"email": "leewoorim@naver.com", "hashed_password": "leewoorim"}


app.dependency_overrides[auth.register_user] = mock_create_user
app.dependency_overrides[auth.get_user] = mock_read_user

client = TestClient(app)


def test_signup_success():
    response = client.post(
        "/auth/signup",
        json={
            "email": "leewoorim@naver.com",
            "hashed_password": "leewoorim",
        },
    )

    assert response.status_code == 200


def test_signup_fail():
    response = client.post(
        "/auth/signup",
        json={
            "email": "leewoorim@naver.com",
            "hashed_password": "leewoorim",
        },
    )

    crud.get_login()

    assert response.status_code == 400, response.text


def test_token_success():
    response = client.get("/auth/token")
    crud.get_user()

    assert response.status_code == 200

    data = response.json()
    assert data["email"] == "leewoorim@naver.com"


def test_token_fail():
    response = client.get(f"/auth/users/{user_id}")

    assert response.status_code == 404
