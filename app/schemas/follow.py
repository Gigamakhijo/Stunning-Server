from typing import List

from pydantic import BaseModel


class FollowBase(BaseModel):
    followee_id: int


class FollowCreate(FollowBase):
    ...


class FollowGet(FollowBase):
    pending: bool
