from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session

from .. import crud, oauth2, schemas

from ..database import get_db
import httpx

router = APIRouter(prefix="/feeds", tags=["feeds"])


@router.post("/", response_model=schemas.FeedGet, status_code=status.HTTP_200_OK)
def create_feed(
    current_user: Annotated[schemas.UserAuth, Depends(oauth2.get_authenticated_user)],
    feed: schemas.FeedCreate,
    db: Session = Depends(get_db),
):
    if current_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    video_url = crud.upload_file(feed.video)
    thumbnail_url = crud.upload_file(feed.thumbnail)

    feed.video = video_url
    feed.thumbnail = thumbnail_url

    return crud.create_feed(db, feed, user_id=current_user.id)


@router.get("/", status_code=status.HTTP_200_OK)
def get_feeds(
    current_user: Annotated[schemas.UserAuth, Depends(oauth2.get_authenticated_user)],
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
):
    if current_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    return crud.get_feeds(db, user_id=current_user.id, skip=skip, limit=limit)


@router.get("/{feed_id}", status_code=status.HTTP_200_OK)
def get_video(
    current_user: Annotated[schemas.UserAuth, Depends(oauth2.get_authenticated_user)],
    feed_id: int,
):
    if current_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    video_url = crud.get_video(feed_id)

    def iterfile():
        with httpx.stream("GET", video_url) as r:
            for chunk in r.iter_bytes():
                yield chunk

    return StreamingResponse(iterfile(), media_type="video/mp4")


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_feed(
    id: int,
    current_user: Annotated[schemas.UserAuth, Depends(oauth2.get_authenticated_user)],
    db: Session = Depends(get_db),
):
    if current_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    feed = crud.get_feed(db, id)

    if feed is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="feed does not exist",
        )

    crud.delete_feed(db, feed.id)
