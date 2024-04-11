#from ..import crud,schemas
from fastapi import APIRouter, HTTPException, status
import datetime
from app.schemas.todo import TodoCreate as create
from app.schemas.todo import TodoGet as get
from app.crud.todo import create_todo as t
#from ..crud import todo as crud_todo
#from ..schemas import todo as schemas_todo
from ..database import connect_to_mysql

conn=connect_to_mysql()
mycursor=conn.cursor()



router=APIRouter(prefix="/todos",tags=["todos"])

@router.post("/",response_model=get ,status_code=status.HTTP_200_OK)
def create_todo(
    todo: create,
    current_user:int,
    ):

    
    if current_user is None:
        raise HTTPException(status_code=401,detail="User not found" )

    return t.create_todo(todo, user_id=current_user)





'''@router.get("/",status_code=status.HTTP_200_OK)
def get_todos(
    db_connection:connection.MySQLConnection,
    current_user : int,
    date: datetime.date
):
    if current_user is None:
        raise HTTPException(status_code=401, detail="User not found")

    current_date=date.today()

    return crud_todo.get_todos_by_date(db_connection, user_id=current_user, date=current_date)







@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_todo(
    id:int,
    current_user:int,
    db_connection:connection.MySQLConnection,
    ):
    if current_user is None:
        raise HTTPException(status_code=401,detail="User not found")
    
    todo=crud_todo.get_todo(db_connection,id)

    if todo is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"todo with id: {id} does not exist,"
        )
    
    crud_todo.delete_todo(db_connection, todo.id)




@router.put("/{id}", response_model=schemas.todo.TodoGet)
def update_todo(
    id:int,
    current_user:int,
    new_todo: schemas.todo.TodoEdit,
    db_connection:connect.MySQLConnection,
):
    
    if current_user is None:
        raise HTTPException(status_code=401, detail="User not found")
    
    todo=crud.todo.get_todo(db_connection,current_user)

    if todo is None:
        raise HTTPException'''
