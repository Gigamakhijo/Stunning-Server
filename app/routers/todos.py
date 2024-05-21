from fastapi import APIRouter, Depends, status,HTTPException
from mysql.connector.connection import MySQLConnection

import datetime
<<<<<<< HEAD
from .. import crud, schemas
from ..database import connect, get_conn, init_todo_db


=======

from fastapi import APIRouter, Depends, HTTPException, status
from mysql.connector.connection import MySQLConnection

from .. import crud, schemas
from ..database import connect, get_conn, init_todo_db
>>>>>>> 3954c7a96d9b40a741312ef6c04b3d20d47da27b

router = APIRouter(prefix="/todos", tags=["todos"])

@router.on_event("startup")  
async def startup_event():
    conn = connect()
    init_todo_db(conn) 

<<<<<<< HEAD
=======
@router.on_event("startup")
async def startup_event():
    conn = connect()
    init_todo_db(conn)
>>>>>>> 3954c7a96d9b40a741312ef6c04b3d20d47da27b


@router.post("/", status_code=status.HTTP_200_OK)
async def create_todo(
    todo: schemas.TodoCreate,
    conn: MySQLConnection = Depends(get_conn),
):
    result = crud.create_todo(conn, todo, todo.user_id)

<<<<<<< HEAD
    return result 



@router.get("/", response_model=schemas.TodoListGet, status_code=status.HTTP_200_OK) #완
async def get_todos( 
    date: datetime.date, 
    days_left:int,
    first:int,
    amount:int,
    conn: MySQLConnection = Depends(get_conn),
): 
    return crud.get_todos_by_date(conn, date, days_left, first, amount, user_id=0)


@router.put("/{id}", response_model=schemas.TodoGet)#완
async def update_todo(
    id: int,
    new_todo: schemas.TodoEdit,
    conn:MySQLConnection = Depends(get_conn),
): 
=======
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
>>>>>>> 3954c7a96d9b40a741312ef6c04b3d20d47da27b
    todo = crud.get_todo(conn, id)

    if todo is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
<<<<<<< HEAD
            detail=f"todo with id: {id} does not exist")
    
    return crud.update_todo(conn, id, new_todo)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)#완
async def delete_todo(
    id: int,
    conn: MySQLConnection = Depends(get_conn),
): 
=======
            detail=f"todo with id: {id} does not exist",
        )

    return crud.update_todo(conn, id, new_todo)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)  # 완
async def delete_todo(
    id: int,
    conn: MySQLConnection = Depends(get_conn),
):
>>>>>>> 3954c7a96d9b40a741312ef6c04b3d20d47da27b
    todo = crud.get_todo(conn, id)

    if todo is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"todo with id: {id} does not exist",
        )
<<<<<<< HEAD
    
=======

>>>>>>> 3954c7a96d9b40a741312ef6c04b3d20d47da27b
    crud.delete_todo(conn, id)
