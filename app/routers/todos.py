import datetime

from fastapi import APIRouter, Depends, HTTPException, status
from mysql.connector.connection import MySQLConnection

from .. import crud, schemas
from ..database import connect, get_conn, init_todo_db

router = APIRouter(prefix="/todos", tags=["todos"])


@router.on_event("startup")
async def startup_event():
    conn = connect()
    init_todo_db(conn)


@router.post("/", status_code=status.HTTP_200_OK)
async def create_todo(
    todo: schemas.TodoCreate,
    conn: MySQLConnection = Depends(get_conn),
):
    result = crud.create_todo(conn, todo, todo.user_id)

    return result


@router.get(
    "/", response_model=schemas.TodoListGet, status_code=status.HTTP_200_OK
)  # 완
async def get_todos(
    date: datetime.date,
    days_left: int,
    first: int,
    amount: int,
    conn: MySQLConnection = Depends(get_conn),
):
    return crud.get_todos_by_date(conn, date, days_left, first, amount, user_id=0)


@router.put("/{id}", response_model=schemas.TodoGet)  # 완
async def update_todo(
    id: int,
    new_todo: schemas.TodoEdit,
    conn: MySQLConnection = Depends(get_conn),
):
    todo = crud.get_todo(conn, id)

    if todo is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"todo with id: {id} does not exist",
        )

    return crud.update_todo(conn, id, new_todo)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)  # 완
async def delete_todo(
    id: int,
    conn: MySQLConnection = Depends(get_conn),
):
    todo = crud.get_todo(conn, id)

    if todo is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"todo with id: {id} does not exist",
        )

    crud.delete_todo(conn, id)
