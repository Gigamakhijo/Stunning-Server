from datetime import datetime
from typing import List

from pydantic import BaseModel


class TodoBase(BaseModel):
    user_id: int


class TodoGet(TodoBase):
    id: int
    icon: str
    title: str
    contents: str
    color: str
    done: bool


class TodoCreate(TodoBase):
    date: datetime | None = None
    icon: str
    title: str
    contents: str
    color: str
    done: bool


class TodoListGet(BaseModel):
    todolist: List[TodoGet]
