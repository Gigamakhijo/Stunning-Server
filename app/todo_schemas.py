from datetime import datetime

from pydantic import BaseModel


class TodoBase(BaseModel):
    date: datetime
    title: str
    contents: str
    place: str
    due_date: datetime
    is_completed: bool


class TodoGet(TodoBase):
    id: int


class TodoCreate(TodoBase):
    user_id: int


class TodoUpdate(TodoBase):
    pass
