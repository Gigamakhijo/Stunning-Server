from sqlalchemy import Column, Integer, String, DateTime

from ..database import Base


class Todo(Base):
    __tablename__ = "todo"

    id = Column(Integer, primary_key=True, nullable=False, index=True)
    date = Column(DateTime)
    title = Column(String)
    icon = Column(String)
    contents = Column(String)
    color = Column(String)
    done = Column(bool)
