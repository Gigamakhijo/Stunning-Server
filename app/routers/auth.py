from fastapi import APIRouter, Security

from ..auth import VerifyToken, UserInfo

router = APIRouter(prefix="/auth", tags="auth")

auth = VerifyToken()
info = UserInfo()

@router.get("/api/public")
def public():
    """No access token required to access this route"""

    result = {
        "status": "sucess",
        "mesaage": (
            "Hello from a public endpoint! You don't need to be "
            "authenticated to see this."
        ),
    }

    return result


@router.get("/api/private")
def private(auth_result: str = Security(auth.verify)):
    info.get_userinfo()
    return auth_result
