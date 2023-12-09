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
    username: str | None
    full_name: str | None = None
    gender: str | None = None
    phone_number: str | None = None
    status_message: str | None = None


class UserEdit(BaseModel):
    username: str | None
    full_name: str | None
    gender: str | None
    phone_number: str | None
    status_message: str | None

    class Config:
        orm_mode = True


class UserGet(UserBase):
    id: int
    username: str | None
    full_name: str | None
    gender: str | None
    phone_number: str | None
    status_message: str | None

    class Config:
        from_attribues = True
