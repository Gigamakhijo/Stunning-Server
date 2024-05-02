from fastapi import APIRouter, Depends, status,HTTPException
from mysql.connector.connection import MySQLConnection

import datetime
from .. import crud, schemas
from ..database import connect, get_conn, init_todo_db



router = APIRouter(prefix="/todos", tags=["todos"])

@router.on_event("startup") #load시에 테이블 만들어짐 
async def startup_event():
    conn = connect()
    init_todo_db(conn) #여기서 db초기화 시키고 



@router.post("/", status_code=status.HTTP_200_OK)
async def create_todo(
    todo: schemas.TodoCreate,
    conn: MySQLConnection = Depends(get_conn),#연결
):
    result = crud.create_todo(conn, todo, todo.user_id)

    return result #없어도 됨



@router.get("/", response_model=schemas.TodoListGet, status_code=status.HTTP_200_OK) #완
async def get_todos( #client가 지금 날짜만 보내줌
    date: datetime.date, #4.29꺼 보냄 
    conn: MySQLConnection = Depends(get_conn),
    #여기 current_user 넣기
): 
    return crud.get_todos_by_date(conn, date, user_id=0)


@router.put("/{id}", response_model=schemas.TodoGet)
async def update_todo(
    id: int,
    new_todo: schemas.TodoEdit,
    conn: MySQLConnection = Depends(get_conn),
): 
    todo = crud.get_todo(conn, id)

    if todo is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"todo with id: {id} does not exist")
    
    return crud.update_todo(conn, id, new_todo)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)#완
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
