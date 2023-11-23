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


class TodoCreate(TodoBase):
    user_id: int


class TodoListGet(BaseModel):
    date: str


class TodoList(TodoListGet):
    todolist: List[TodoBase]
