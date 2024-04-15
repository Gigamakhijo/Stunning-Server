from datetime import datetime
from typing import List

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


class TodoEdit(TodoCreate):
    pass


class TodoListGet(BaseModel):
    todos: List[TodoGet]
