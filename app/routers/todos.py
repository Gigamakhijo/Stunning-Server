import datetime
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from .. import crud, oauth2, schemas
from ..database import get_db

router = APIRouter(prefix="/todos", tags=["todos"])


@router.post("/", response_model=schemas.TodoGet, status_code=status.HTTP_200_OK)
def create_todo(
    current_user: Annotated[schemas.UserAuth, Depends(oauth2.get_authenticated_user)],
    todo: schemas.TodoCreate,
    db: Session = Depends(get_db),
):
    if current_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    return crud.create_todo(db, todo, user_id=current_user.id)


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

    return crud.get_todos_by_date(
        db, date, skip=skip, limit=limit, user_id=current_user.id
    )


@router.put("/{id}", response_model=schemas.TodoGet)
def update_todo(
    id: int,
    current_user: Annotated[schemas.UserAuth, Depends(oauth2.get_authenticated_user)],
    new_todo: schemas.TodoEdit,
    db: Session = Depends(get_db),
):
    if current_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    todo = crud.get_todo(db, id)

    if todo is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"todo with id: {id} does not exist",
        )

    return crud.update_todo(db, new_todo, todo_id=todo.id)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_todo(
    id: int,
    current_user: Annotated[schemas.UserAuth, Depends(oauth2.get_authenticated_user)],
    db: Session = Depends(get_db),
):
    if current_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    todo = crud.get_todo(db, id)

    if todo is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"todo with id: {id} does not exist",
        )
