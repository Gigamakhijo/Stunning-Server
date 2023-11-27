from pydantic import BaseModel


class FeedCreate(BaseModel):
    user_id: int
    video: str
    concentration: int
    thumnail: str
