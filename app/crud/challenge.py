from .. import schemas
from mysql.connector.connection import MySQLConnection

import datetime



def create_challenge(conn:MySQLConnection, challenge:schemas.ChallengeCreate, user_id:int):
    cursor=conn.cursor() 

    values=(
        challenge.title,
        challenge.is_completed,
        challenge.date,
        challenge.due_date,
        user_id
    )

    insert_query="""
    INSERT INTO challenge 
    (title, is_completed, date, due_date, user_id)
    VALUES (%s, %s, %s, %s, %s)"""

    
    cursor.execute(insert_query,values)

    conn.commit()
    
    return challenge


def get_challenge(conn:MySQLConnection , challenge_id:int):

    cursor=conn.cursor()

    query="SELECT * FROM challenge WHERE id= %s "

    cursor.execute(query, (challenge_id,))

    challenge = cursor.fetchone()

    keys = ["id", "date", "due_date", "title", "is_completed","user_id"]

    challenge_dict={}

    for key, value in zip(keys, challenge):
        challenge_dict[key] = value

    return challenge_dict

     

#user_id는 challenge다 갖고오기 위한
def get_challenges_by_date(conn:MySQLConnection, date:datetime.date, days_left:int, first:int, amount:int, user_id:int):

    cursor=conn.cursor(dictionary=True)

    duration = date + datetime.timedelta(days=days_left)

    query="""
    SELECT title, is_completed, date, due_date, id 
    FROM challenge
    WHERE user_id = %s
    AND due_date >= %s
    AND due_date < %s
    ORDER BY due_date ASC
    LIMIT %s, %s
    """
    
   
    values=(user_id, date, duration, first, amount)
    
    cursor.execute(query, values)

    challenge_dict = [] #튜플의 리스트로 넣기 
    for row in cursor:
        challenge_dict.append(row)

    return {"challenges" : challenge_dict}

    

def delete_challenge(conn:MySQLConnection, challenge_id:int):

    cursor=conn.cursor()

    delete_query="DELETE FROM challenge WHERE id=%s"

    cursor.execute(delete_query, (challenge_id,))

    conn.commit()


def update_challenge(conn: MySQLConnection, challenge_id:int, new_challenge:schemas.ChallengeEdit):

    cursor=conn.cursor()

    update_query="""
    UPDATE challenge
    SET title = %s, is_completed = %s, date = %s, due_date = %s
    WHERE id = %s"""

    values=(
        new_challenge.title,
        new_challenge.is_completed,
        new_challenge.date,
        new_challenge.due_date,
        challenge_id

    )

    cursor.execute(update_query, values)

    conn.commit()

    return get_challenge(conn, challenge_id)

   

    


    

    