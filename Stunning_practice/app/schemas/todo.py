from datetime import datetime
from pydantic import BaseModel


class TodoBase(BaseModel):
    date:datetime
    title:str
    contents:str
    place:str
    due_date:datetime
    is_completed:bool


class TodoCreate(TodoBase):
    ...


class TodoGet(TodoBase):
    id:int
    user_id:int

class TodoEdit(TodoBase):
    ...
    

    




