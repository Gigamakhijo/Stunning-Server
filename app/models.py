from pydantic import BaseModel


class User(BaseModel):
    email: str
    hashed_password: str

    class Config:
        from_attributes = True
