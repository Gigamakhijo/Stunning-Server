from datetime import datetime
from typing import List

from pydantic import BaseModel


class TodoBase(BaseModel):
    date: datetime
    due_date: datetime
    title: str
    contents: str
    place: str
    is_completed: bool


class TodoGet(TodoBase):
    id: int


class TodoCreate(TodoBase):
    user_id: int


class TodoUpdate(TodoBase):
    pass


class TodoListGet(BaseModel):
    todos: List[TodoGet]