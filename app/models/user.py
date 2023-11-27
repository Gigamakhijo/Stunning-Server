from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, backref

from ..database import Base
from .follow import Follow


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

    todos = relationship("Todo", backref="owner", lazy="dynamic")
    followed = relationship(
        "User",
        seondary=Follow,
        primaryjoin=(Follow.c.follower_id == id),
        secondaryjoin=(Follow.c.followed_id == id),
        backref=backref("Follow", lazy="dynamic"),
        lazy="dynamic",
    )
