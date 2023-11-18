from fastapi.testclient import testclient

from .. import routers
from ..main import app

from .. import schemas


def mock_create_user():
    return schemas.user(
        id=1,
        username="test_user",
        email="test_user@test.com",
        gender="female",
        phone_number=123456789,
        status_message="sldkfjalskfjalksdjfkajsdklfjasdkf",
    )


app.dependency_overrides[routers.users.create_user] = mock_create_user

client = testclient(app)


def test_signup_success():
    response = client.post(
        "/users/",
        json={
            "email": "leewoorim@naver.com",
            "hashed_password": "leewoorim",
        },
    )

    assert response.status_code == 200
