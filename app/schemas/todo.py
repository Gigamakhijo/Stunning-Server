from typing import List
from datetime import datetime

from pydantic import BaseModel


class Todo(BaseModel):
    date: datetime
    icon: str
    title: str
    contents: str
    color: str
    done: bool


class TodoListGet(BaseModel):
    date: str


class TodoList(TodoListGet):
    todolist: List[Todo]
