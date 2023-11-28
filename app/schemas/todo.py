from datetime import datetime
from typing import List

from pydantic import BaseModel


class TodoBase(BaseModel):
    date: datetime
    icon: str
    title: str
    contents: str
    color: str
    done: bool


class TodoGet(TodoBase):
    id: int
    user_id: int


class TodoCreate(TodoBase):
    ...


class TodoEdit(TodoCreate):
    ...


class TodoListGet(BaseModel):
    todolist: List[TodoGet]
