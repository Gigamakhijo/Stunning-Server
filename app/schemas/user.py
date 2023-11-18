from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None


class User(BaseModel):
    id: int | None = None
    username: str
    email: str | None = None
    full_name: str | None = None
    gender: int | None = None
    phone_number: str | None = None
    status_message: str | None = None


class UserInDB(User):
    hashed_password: str
