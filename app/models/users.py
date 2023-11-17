from pydantic import BaseModel

class Token(BaseModel):
    access_token: str
    token_type: str

class Login(BaseModel):
    email: str
    password: str

    class Config():
        from_attributes: True

class User(BaseModel):
    email: str
    hashed_password: str

    class Config():
        from_attributes: True

