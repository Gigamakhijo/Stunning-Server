from datetime import datetime
from typing import List

from pydantic import BaseModel


class CommentBase(BaseModel):
<<<<<<< HEAD
    date:datetime
    contents:str
    title:str


class CommentCreate(CommentBase):
    user_id:int


class CommentGet(CommentBase):
    id:int
    user_id:int


class CommentEdit(CommentBase):
    ...



class CommentListGet(BaseModel):
    comments:List[CommentGet]


=======
    date: datetime
    contents: str
    title: str


class CommentCreate(CommentBase):
    user_id: int


class CommentGet(CommentBase):
    id: int
    user_id: int


class CommentEdit(CommentBase): ...


class CommentListGet(BaseModel):
    comments: List[CommentGet]
>>>>>>> 3954c7a96d9b40a741312ef6c04b3d20d47da27b
