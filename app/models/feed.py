from sqlalchemy import Column, Integer, DateTime, String, ForeignKey
from sqlalchemy.orm import relationship

import datetime

from ..database import Base


class Feed(Base):
    __tablename__ = "feeds"

    id = Column(Integer, primary_key=True, nullable=False, index=True)
    date = Column(DateTime, default=datetime.datetime.utcnow)
    video = Column(String)
    thumbnail = Column(String)
    concentration = Column(Integer)

    user_id = Column(Integer, ForeignKey("users.id"))
    users = relationship("User", back_populates="feeds")
