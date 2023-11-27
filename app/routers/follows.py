from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from .. import crud, oauth2, schemas
from ..database import get_db

router = APIRouter(prefix="/follows", tags=["follows"])


@router.post("/", status_code=status.HTTP_200_OK)
def create_follow(
    current_user: Annotated[schemas.UserGet, Depends(oauth2.get_authenticated_user)],
    folowee_id: schemas.FollowCreate,
    db: Session = Depends(get_db),
):
    if current_user is None:
        raise HTTPException(status_code=404, detail="User not found")


@router.get("/", status_code=status.HTTP_200_OK)
def get_follows(
    current_user: Annotated[schemas.UserGet, Depends(oauth2.get_authenticated_user)],
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
):
    if current_user is None:
        raise HTTPException(status_code=404, detail="User not found")
