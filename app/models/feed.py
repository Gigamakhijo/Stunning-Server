import datetime

from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from ..database import Base


class Feed(Base):
    __tablename__ = "feeds"

    id = Column(Integer, primary_key=True, nullable=False, index=True)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
    video_url = Column(String, nullable=False)
    thumbnail_url = Column(String, nullable=False)
    concentration = Column(Float, nullable=True)

    user_id = Column(Integer, ForeignKey("users.id"))