from fastapi.testclient import TestClient

from ..routers import users 
from ..main import app

from .. import schemas


def mock_create_user():
    return schemas.user(
        email="test_user@test.com"
    )


app.dependency_overrides[users.create_user] = mock_create_user

client = TestClient(app)


def test_signup_success():
    response = client.post(
        "/users/",
        json={
            "email": "leewoorim@naver.com",
            "hashed_password": "leewoorim",
        },
    )

    assert response.status_code == 200
