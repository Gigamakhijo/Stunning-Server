from fastapi import APIRouter, Depends, HTTPException, status
from mysql.connector.connection import MySQLConnection

import datetime
from .. import schemas, crud
from ..database import connect, get_conn, init_challenge_db


router=APIRouter(prefix="/challenges", tags=["challenges"])

@router.on_event("startup")
async def startup_event():
    conn = connect()
    init_challenge_db(conn)

    
@router.post("/", status_code=status.HTTP_200_OK)#완
async def create_challenge(
    challenge:schemas.ChallengeCreate,
    conn:MySQLConnection = Depends(get_conn)
):
    
    result = crud.create_challenge(conn, challenge, user_id=0)

    return result


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)#완
async def delete_challenge (
    id:int,
    conn: MySQLConnection = Depends(get_conn),
):
    
    challenge = crud.get_challenge(conn, id)

    if challenge is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"challenge with id: {id} does not exist",
        )
    
    crud.delete_challenge(conn, id)


@router.get("/", response_model= schemas.ChallengeListGet, status_code=status.HTTP_200_OK)#완
async def get_challenge(
    date:datetime.date,
    days_left:int,
    first:int,
    amount:int, 
    conn:MySQLConnection = Depends(get_conn),
):
    
    return crud.get_challenges_by_date(conn, date, days_left, first, amount, user_id=0)
    

@router.put("/{id}", response_model=schemas.ChallengeGet)#완
async def update_challenge(
    id:int,
    new_challenge:schemas.ChallengeEdit,
    conn:MySQLConnection=Depends(get_conn),
):
    challenge=crud.get_challenge(conn, id)

    if challenge is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"challenge with id: {id} does not exist"
        )
    
    return crud.update_challenge(conn, id, new_challenge)

    
    
    

    



    

    
    
    





