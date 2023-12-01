from datetime import datetime

from pydantic import BaseModel


class FeedBase(BaseModel):
    date: datetime
    video: str
    thumnail: str
    concentration: int


class FeedCreate(FeedBase):
    ...


class FeedGet(FeedBase):
    id: int
