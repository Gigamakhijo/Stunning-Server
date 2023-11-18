from fastapi.testclient import TestClient

from .. import oauth2, schemas
from ..main import app
from ..routers.auth import get_current_user

email = "test@example.com"
password = "test_password"


def override_get_current_user():
    return schemas.UserAuth(
        email=email,
        hashed_password=oauth2.get_password_hash(password),
    )


app.dependency_overrides[get_current_user] = override_get_current_user


client = TestClient(app)


def test_token_success():
    response = client.post(
        "/auth/token", data={"username": email, "password": password}
    )

    assert response.status_code == 200, response.text


def test_token_wrong_password():
    response = client.post(
        "/auth/token", data={"username": email, "password": password + "a"}
    )

    assert response.status_code == 401, response.text
