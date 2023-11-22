from sqlalchemy import Column, Integer, String, Boolean

from ..database import Base


class Todo(Base):
    __tablename__ = "todo"

    id = Column(Integer, primary_key=True, nullable=False, index=True)
    date = Column(String)
    title = Column(String)
    icon = Column(String)
    contents = Column(String)
    color = Column(String)
    done = Column(Boolean)
