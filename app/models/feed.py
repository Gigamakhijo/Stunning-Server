import datetime

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from ..database import Base


class Feed(Base):
    __tablename__ = "feeds"

    id = Column(Integer, primary_key=True, nullable=False, index=True)
    date = Column(DateTime, default=datetime.datetime.utcnow)
    video = Column(String)
    thumnail = Column(String)
    concentration = Column(Integer)

    user_id = Column(Integer, ForeignKey("users.id"))
    users = relationship("User", back_populates="feeds")
