from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from .. import crud, schemas
from ..database import get_db
from ..routers.auth import get_current_user

router = APIRouter(prefix="/users")


@router.post("/", response_model=schemas.UserCreate)
def create_user(
    user: schemas.UserCreate,
    db: Session = Depends(get_db),
):
    db_user = crud.get_user_by_email(db, email=user.email)

    if db_user:
        raise HTTPException(status_code=400, detail="User already registered")

    return crud.create_user(db=db, user=user)


@router.get("/{user_id}", response_model=schemas.UserGet)
def get_user(
    user_id: int,
    current_user: Annotated[schemas.UserAuth, Depends(get_current_user)],
):
    if current_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    return current_user
