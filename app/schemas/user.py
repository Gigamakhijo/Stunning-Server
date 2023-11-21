from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str | None = None


class UserBase(BaseModel):
    email: str


class UserAuth(UserBase):
    hashed_password: str


class UserCreate(UserBase):
    password: str


class UserGet(UserBase):
    id: int
    username: str | None = None
    full_name: str | None = None
    gender: str | None = None
    phone_number: str | None = None
    status_message: str | None = None

    class Config:
        orm_mode = True
