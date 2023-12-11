from typing import List

from pydantic import BaseModel


class FollowBase(BaseModel):
    follower_id: int


class FollowCreate(FollowBase):
    ...


class FollowGet(FollowBase):
    ...
