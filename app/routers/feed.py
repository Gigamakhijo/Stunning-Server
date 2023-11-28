from typing import Annotated

from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session

from .. import crud, schemas, oauth2
from ..database import get_db

router = APIRouter(prefix="/feeds", tags=["feeds"])


@router.post("/", response_model=schemas.FeedCreate, status_code=status.HTTP_200_OK)
def add_feed(
    current_user: Annotated[schemas.UserGet, Depends(oauth2.get_authenticated_user)],
    feed: schemas.FeedCreate,
    db: Session = Depends(get_db),
):
    if current_user is None:
        raise HTTPException(status_code=404, detail="User not found")

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

    feeds = crud.get_feeds(db, user_id=current_user.id, skip=skip, limit=limit)
    return feeds
