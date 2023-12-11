from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship

from ..database import Base

follows = Table(
    "follows",
    Base.metadata,
    Column("follower_id", ForeignKey("users.id"), primary_key=True),
    Column("following_id", ForeignKey("users.id"), primary_key=True),
)


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

    profile_image = Column(String)

    followers = relationship(
        "User",
        secondary="follows",
        primaryjoin="User.id==follows.c.following_id",
        secondaryjoin="User.id==follows.c.follower_id",
        backref="following",
    )
