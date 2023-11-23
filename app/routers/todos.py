import datetime
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from .. import crud, oauth2, schemas
from ..database import get_db

router = APIRouter(prefix="/todos", tags=["todos"])


@router.post("/", response_model=schemas.UserGet, status_code=status.HTTP_201_CREATED)
def create_todo(
    todo: schemas.TodoCreate,
    current_user: Annotated[schemas.UserAuth, Depends(oauth2.get_authenticated_user)],
):
    if current_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    return crud.create_user(
        db=db,
        user=schemas.UserCreate(
            email=user.email,
            password=user.password,
        ),
    )


@router.get("/", response_model=schemas.TodoListGet, status_code=status.HTTP_200_OK)
def get_todos(
    current_user: Annotated[schemas.UserAuth, Depends(oauth2.get_authenticated_user)],
    date: datetime.date,
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
):
    if current_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    todos = crud.get_todos_by_date(db, date, skip=skip, limit=limit)
    breakpoint()
    return todos
