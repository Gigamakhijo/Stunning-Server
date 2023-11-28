from pydantic import BaseModel

class FeedBase(BaseModel):
    video: str
    concentration: int
    thumnail: str

class FeedCreate(FeedBase):
    ...

class FeedGet(FeedBase):
    user_id: int