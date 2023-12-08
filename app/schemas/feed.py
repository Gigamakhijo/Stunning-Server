from datetime import datetime

from pydantic import BaseModel


class FeedBase(BaseModel):
    timestamp: datetime


class FeedCreate(FeedBase):
    video_url: str
    thumbnail_url: str


class FeedGet(FeedBase):
    id: int
    video_url: str
    thumbnail_url: str
    concentration: float | None
