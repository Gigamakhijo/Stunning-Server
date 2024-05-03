from fastapi import APIRouter, Depends, HTTPException, status
from mysql.connector.connection import MySQLConnection

import datetime
from .. import schemas, crud
from .. database import connect, get_conn, init_comment_db


router = APIRouter(prefix="/comments", tags=["comments"])


@router.on_event("startup")
async def startup_event():
    conn = connect()
    init_comment_db(conn)


@router.post("/", status_code=status.HTTP_200_OK)#완
async def create_comment(
    comment:schemas.CommentCreate,
    conn:MySQLConnection = Depends(get_conn)
):
    result = crud.create_comment(conn, comment, user_id = 0)

    return result


@router.get("/", response_model=schemas.CommentListGet, status_code=status.HTTP_200_OK)#완
async def get_comments(
    first_date:datetime.date,
    last_date:datetime.date,
    first_index:int,
    amount:int,
    conn:MySQLConnection = Depends(get_conn),   
):
    
    comment = crud.get_comments_by_date(first_date, last_date, first_index, amount, conn, user_id=0)

    return comment


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)#완
async def delete_comment(
    id:int,
    conn:MySQLConnection = Depends(get_conn),
): 
    
    comment = crud.get_comment(id, conn)

    if comment is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"comment with id: {id} does not exist"
        )
    
    crud.delete_comment(conn, id)


@router.put("/{id}", response_model=schemas.CommentGet)#완
async def update_comment(
    id:int,
    update_comment:schemas.CommentEdit,
    conn:MySQLConnection = Depends(get_conn),
):
    comment = crud.get_comment(id, conn)

    if comment is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"comment with id: {id} does not exist"
        )
    
    return crud.update_comment(conn, update_comment, id)

    

    
    
