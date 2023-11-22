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

class TodoList(Todo):
    todolist:List[Todo]

class TodoListGet(BaseModel):
    date: str