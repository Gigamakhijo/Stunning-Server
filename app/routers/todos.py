from fastapi import APIRouter, Depends, status
from mysql.connector.connection import MySQLConnection

from .. import crud, schemas
from ..database import connect, get_conn, init_db

router = APIRouter(prefix="/todos", tags=["todos"])


@router.on_event("startup")
async def startup_event():
    conn = connect()
    init_db(conn)


@router.post("/", status_code=status.HTTP_200_OK)
async def create_todo(
    todo: schemas.TodoCreate,
    conn: MySQLConnection = Depends(get_conn),
):
    result = crud.create_todo(conn, todo, user_id=0)


@router.get("/", response_model=schemas.TodoListGet, status_code=status.HTTP_200_OK)
async def get_todos(
    skip: int = 0,
    limit: int = 100,
    conn: MySQLConnection = Depends(get_conn),
):
    return crud.get_todo(conn, user_id=0)


@router.put("/{id}", response_model=schemas.TodoGet)
async def update_todo(
    id: int,
    new_todo: schemas.TodoEdit,
    conn: MySQLConnection = Depends(get_conn),
): ...


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(
    id: int,
    conn: MySQLConnection = Depends(get_conn),
): ...
