from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: str


class Login(BaseModel):
    email: str
    password: str

    class Config:
        from_attributes: True


class Profile(BaseModel):
    email: str
    username: str
    gender: int
    phone_number: str
