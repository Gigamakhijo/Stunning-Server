from sqlalchemy import Column, Integer, String

from ..database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False, index=True)
    email = Column(String, unique=True, index=True)
    username = Column(String)
    full_name = Column(String)
    gender = Column(String)
    phone_number = Column(String)
    status_message = Column(String)
    hashed_password = Column(String, nullable=False)
