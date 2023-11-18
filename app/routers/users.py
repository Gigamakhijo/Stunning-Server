from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from .. import crud, oauth2, schemas
from ..database import get_db

router = APIRouter(prefix="/users")


@router.post("/", response_model=schemas.UserGet, status_code=status.HTTP_201_CREATED)
def create_user(
    user: schemas.UserCreate,
    db: Session = Depends(get_db),
):
    db_user = crud.get_user_by_email(db, email=user.email)

    if db_user:
        raise HTTPException(status_code=400, detail="User already registered")

    return crud.create_user(
        db=db,
        user=schemas.UserCreate(
            email=user.email,
            password=user.password,
        ),
    )


@router.get("/me", response_model=schemas.UserGet)
def get_user(
    current_user: Annotated[schemas.UserAuth, Depends(oauth2.get_authenticated_user)],
):
    if current_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    return current_user
