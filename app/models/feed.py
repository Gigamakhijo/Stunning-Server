from sqlalchemy import Column, Integer, String

from ..database import Base


class Feed(Base):
    __tablename__ = "feed"

    id = Column(Integer, primary_key=True, nullable=False, index=True)
    user_id = Column(Integer, index=True)
    video = Column(String)
    concentration = Column(Integer)
    thumnail = Column(String)
