from sqlalchemy import Column, Integer, String, ForeignKey

from ..database import Base


class Feed(Base):
    __tablename__ = "feed"

    id = Column(Integer, primary_key=True, nullable=False, index=True)
    video = Column(String)
    concentration = Column(Integer)
    thumnail = Column(String)

    user_id = Column(Integer, ForeignKey("users.id"))