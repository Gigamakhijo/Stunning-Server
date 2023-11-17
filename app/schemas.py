from sqlalchemy import Column, Integer, String
from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True,autoincrement=True)
    username = Column(String, unique=True,index=True)
    email = Column(String, unique=True, index=True)
    gender = Column(bool)
    phone_number = Column(String)
    state_message = Column(String)
    hashed_password = Column(String)
    

