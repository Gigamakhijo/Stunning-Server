from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from .. import crud, oauth2, s3, schemas
from ..config import settings
from ..database import get_db

router = APIRouter(prefix="/feeds", tags=["feeds"])


@router.post("/thumbnail_url/{object_name}", status_code=status.HTTP_201_CREATED)
def create_thumbnail_post_url(
    current_user: Annotated[schemas.UserAuth, Depends(oauth2.get_authenticated_user)],
    object_name: str,
):
    if current_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    return s3.create_presigned_post(settings.bucket_name, object_name, expiration=3600)


@router.post("/video_url/{object_name}", status_code=status.HTTP_201_CREATED)
def create_video_post_url(
    current_user: Annotated[schemas.UserAuth, Depends(oauth2.get_authenticated_user)],
    object_name: str,
):
    if current_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    return s3.create_presigned_post(settings.bucket_name, object_name, expiration=3600)


@router.post("/", response_model=schemas.FeedGet, status_code=status.HTTP_201_CREATED)
def create_feed(
    current_user: Annotated[schemas.UserGet, Depends(oauth2.get_authenticated_user)],
    feed: schemas.FeedCreate,
    db: Session = Depends(get_db),
):
    if current_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    return crud.create_feed(db=db, feed=feed, user_id=current_user.id)


@router.get("/{feed_id}", status_code=status.HTTP_200_OK)
def get_feed(
    current_user: Annotated[schemas.UserAuth, Depends(oauth2.get_authenticated_user)],
    feed_id: int,
    db: Session = Depends(get_db),
):
    if current_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    feed = crud.get_feed(db=db, feed_id=feed_id)

    if feed is None:
        raise HTTPException(status_code=404, detail="Feed not found")

    return feed


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


@router.delete("/{feed_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_feed(
    feed_id: int,
    current_user: Annotated[schemas.UserAuth, Depends(oauth2.get_authenticated_user)],
    db: Session = Depends(get_db),
):
    if current_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    feed = crud.get_feed(db, feed_id=feed_id)

    if feed is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="feed does not exist",
        )

    if feed.user_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Access forbidden"
        )

    crud.delete_feed(db, feed_id=feed.id)
