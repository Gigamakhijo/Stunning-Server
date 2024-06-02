from typing import Optional
import jwt
from .config import settings
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer, SecurityScopes
import requests

class UnauthroizedException(HTTPException):
    def __init__(self, detail: str, **kwargs):
        super().__init__(status.HTTP_403_FORBIDDEN, detail=detail)


class UnauthenticatedException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Requires authentication"
        )


class VerifyToken:
    def __init__(self):
        jsonurl = f"https://{settings.auth0_domain}/.well-known/jwks.json"
        self.jwks_client = jwt.PyJWKClient(jsonurl)

    async def verify(
        self,
        security_scopes: SecurityScopes,
        token: Optional[HTTPAuthorizationCredentials] = Depends(HTTPBearer()),
    ):
        if token is None:
            raise UnauthenticatedException

        try:
            signing_key = self.jwks_client.get_signing_key_from_jwt(
                token.credentials
            ).key
        except jwt.exceptions.PyJWKClientError as error:
            raise UnauthroizedException(str(error))
        except jwt.exceptions.DecodeError as error:
            raise UnauthroizedException(str(error))

        try:
            payload = jwt.decode(
                token.credentials,
                signing_key,
                algorithms=settings.auth0_algorithms,
                audience=settings.auth0_api_audience,
                issuer=settings.auth0_issuer,
            )
        except Exception as error:
            raise UnauthroizedException(str(error))

        return payload

class UserInfo:
     def __init__(self):
        self.config = settings()
        jwks_url = f'https://{self.config.auth0_domain}/.well-known/jwks.json'
        self.jwks_client = jwt.PyJWKClient(jwks_url)
        userinfo_url = f'https://{self.config.auth0_domain}/userinfo'

     async def get_userinfo(self, security_scopes: SecurityScopes,
                     access_token: Optional[HTTPAuthorizationCredentials] = Depends(HTTPBearer())
                     ):
         headers = {
            "Authorization": f"Bearer {access_token}"
        }
         response = requests.get(self.userinfo_url, headers=headers)
         if response.status_code == 200:
            userinfo = response.json()
            print(userinfo)
         else:
            print(f"Failed to fetch user info: {response.status_code}")