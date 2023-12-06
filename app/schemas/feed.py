from datetime import datetime

from pydantic import BaseModel


class FeedBase(BaseModel):
    date: datetime
    video: str
    thumbnail: str
    concentration: int


class FeedCreate(FeedBase):
    ...


class FeedGet(FeedBase):
    id: int
