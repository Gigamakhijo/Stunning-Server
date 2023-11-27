import datetime
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from .. import crud, oauth2, schemas
from ..database import get_db

router = APIRouter(prefix="/todos", tags=["todos"])


@router.post("/", response_model=schemas.TodoCreate, status_code=status.HTTP_200_OK)
def create_todo(
    current_user: Annotated[schemas.UserGet, Depends(oauth2.get_authenticated_user)],
    todo: schemas.TodoCreate,
    db: Session = Depends(get_db),
):
    if current_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    return crud.create_todo(db, todo)


@router.get("/", status_code=status.HTTP_200_OK)
def get_todos(
    current_user: Annotated[schemas.UserAuth, Depends(oauth2.get_authenticated_user)],
    date: datetime.date,
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
):
    if current_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    todos = crud.get_todos_by_date(db, current_user.id, date, skip=skip, limit=limit)
    return todos


@router.put("/", response_model=schemas.TodoCreate)
def modify_todo(
    current_user: Annotated[schemas.UserGet, Depends(oauth2.get_authenticated_user)],
    todo_id: schemas.TodoIdGet,
    todo: schemas.TodoCreate,
    db: Session = Depends(get_db),
):
    if current_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    return crud.modify_todo(db, todo_id, todo)


@router.delete("/", status_code=status.HTTP_204_NO_CONTENT)
def delete_todo(
    current_user: Annotated[schemas.UserGet, Depends(oauth2.get_authenticated_user)],
    todo_id: int,
    db: Session = Depends(get_db),
):
    if current_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    return crud.delete_todo(db, todo_id)
