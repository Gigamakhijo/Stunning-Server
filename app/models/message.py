from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship

from ..database import Base

follows = Table(
    "follows",
    Base.metadata,
    Column("follower_id", ForeignKey("users.id"), primary_key=True),
    Column("following_id", ForeignKey("users.id"), primary_key=True),
)


class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, nullable=False, index=True)
    content = Column(String, nullable=False)

    followers = relationship(
        "User",
        secondary="follows",
        primaryjoin="User.id==follows.c.following_id",
        secondaryjoin="User.id==follows.c.follower_id",
        backref="following",
    )
