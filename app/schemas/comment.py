from datetime import datetime
from typing import List

from pydantic import BaseModel


class CommentBase(BaseModel):
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


