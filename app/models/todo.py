import datetime

from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String

from ..database import Base


class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, nullable=False, index=True)
    date = Column(DateTime, default=datetime.datetime.utcnow)
    title = Column(String)
    icon = Column(String)
    contents = Column(String)
    color = Column(String)
    done = Column(Boolean)

    user_id = Column(Integer, ForeignKey("users.id"))
