from datetime import datetime
from typing import List

from pydantic import BaseModel


class TodoBase(BaseModel):
    date: datetime
    due_date: datetime
<<<<<<< HEAD
    title: str 
=======
    title: str
>>>>>>> 3954c7a96d9b40a741312ef6c04b3d20d47da27b
    contents: str
    place: str
    is_completed: bool


class TodoGet(TodoBase):
    id: int
<<<<<<< HEAD
    

class TodoCreate(TodoBase):
    user_id: int

class TodoEdit(TodoBase):
    ...


=======


class TodoCreate(TodoBase):
    user_id: int


class TodoEdit(TodoBase): ...


>>>>>>> 3954c7a96d9b40a741312ef6c04b3d20d47da27b
class TodoListGet(BaseModel):
    todos: List[TodoGet]
