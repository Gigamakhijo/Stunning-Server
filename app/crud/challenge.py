<<<<<<< HEAD
from .. import schemas
from mysql.connector.connection import MySQLConnection

import datetime



def create_challenge(conn:MySQLConnection, challenge:schemas.ChallengeCreate, user_id:int):
    
    cursor=conn.cursor()
    
    insert_query="""
    INSERT INTO challenge (date, due_date, title, is_completed, user_id)
    VALUES (%s, %s, %s, %s, %s)"""

    values=(
=======
import datetime

from mysql.connector.connection import MySQLConnection

from .. import schemas


def create_challenge(
    conn: MySQLConnection, challenge: schemas.ChallengeCreate, user_id: int
):
    cursor = conn.cursor()

    insert_query = """
    INSERT INTO challenge (date, due_date, title, is_completed, user_id)
    VALUES (%s, %s, %s, %s, %s)"""

    values = (
>>>>>>> 3954c7a96d9b40a741312ef6c04b3d20d47da27b
        challenge.date,
        challenge.due_date,
        challenge.title,
        challenge.is_completed,
<<<<<<< HEAD
        user_id
    )
    
    cursor.execute(insert_query, values)

    conn.commit()
    
    return challenge


def get_challenge(conn:MySQLConnection ,challenge_id:int):

    cursor=conn.cursor(dictionary=True)

    query="""
=======
        user_id,
    )

    cursor.execute(insert_query, values)

    conn.commit()

    return challenge


def get_challenge(conn: MySQLConnection, challenge_id: int):
    cursor = conn.cursor(dictionary=True)

    query = """
>>>>>>> 3954c7a96d9b40a741312ef6c04b3d20d47da27b
    SELECT id, date, due_date, title, is_completed, user_id
    FROM challenge 
    WHERE id = %s """

    cursor.execute(query, (challenge_id,))

    challenge = cursor.fetchone()

    return challenge

<<<<<<< HEAD
     

#user_id는 challenge다 갖고오기 위한
def get_challenges_by_date(conn:MySQLConnection, date:datetime.date, days_left:int, first:int, amount:int, user_id:int):

    cursor=conn.cursor(dictionary=True)

    duration = date + datetime.timedelta(days=days_left)

    #duration의 00:00:00
    duration_start = datetime.datetime.combine(duration, datetime.time.min)

    #duration의 23:59:59
    duration_end = datetime.datetime.combine(duration, datetime.time.max)

    query="""
=======

# user_id는 challenge다 갖고오기 위한
def get_challenges_by_date(
    conn: MySQLConnection,
    date: datetime.date,
    days_left: int,
    first: int,
    amount: int,
    user_id: int,
):
    cursor = conn.cursor(dictionary=True)

    duration = date + datetime.timedelta(days=days_left)

    # duration의 00:00:00
    duration_start = datetime.datetime.combine(duration, datetime.time.min)

    # duration의 23:59:59
    duration_end = datetime.datetime.combine(duration, datetime.time.max)

    query = """
>>>>>>> 3954c7a96d9b40a741312ef6c04b3d20d47da27b
    SELECT title, is_completed, date, due_date, id 
    FROM challenge
    WHERE user_id = %s
    AND due_date >= %s
    AND due_date <= %s
    ORDER BY due_date ASC
    LIMIT %s, %s
    """
<<<<<<< HEAD
    
    values=(user_id, duration_start, duration_end, first, amount)
    
    cursor.execute(query, values)

    challenge_dict = [] #튜플의 리스트로 넣기 
    for row in cursor:
        challenge_dict.append(row)

    return {"challenges" : challenge_dict}

    

def delete_challenge(conn:MySQLConnection, challenge_id:int):

    cursor=conn.cursor()

    delete_query="DELETE FROM challenge WHERE id=%s"
=======

    values = (user_id, duration_start, duration_end, first, amount)

    cursor.execute(query, values)

    challenge_dict = []  # 튜플의 리스트로 넣기
    for row in cursor:
        challenge_dict.append(row)

    return {"challenges": challenge_dict}


def delete_challenge(conn: MySQLConnection, challenge_id: int):
    cursor = conn.cursor()

    delete_query = "DELETE FROM challenge WHERE id=%s"
>>>>>>> 3954c7a96d9b40a741312ef6c04b3d20d47da27b

    cursor.execute(delete_query, (challenge_id,))

    conn.commit()


<<<<<<< HEAD
def update_challenge(conn: MySQLConnection, challenge_id:int, new_challenge:schemas.ChallengeEdit):

    cursor=conn.cursor()

    update_query="""
=======
def update_challenge(
    conn: MySQLConnection, challenge_id: int, new_challenge: schemas.ChallengeEdit
):
    cursor = conn.cursor()

    update_query = """
>>>>>>> 3954c7a96d9b40a741312ef6c04b3d20d47da27b
    UPDATE challenge
    SET date = %s, due_date = %s, title = %s, is_completed = %s
    WHERE id = %s"""

<<<<<<< HEAD
    values=(
=======
    values = (
>>>>>>> 3954c7a96d9b40a741312ef6c04b3d20d47da27b
        new_challenge.date,
        new_challenge.due_date,
        new_challenge.title,
        new_challenge.is_completed,
<<<<<<< HEAD
        challenge_id
=======
        challenge_id,
>>>>>>> 3954c7a96d9b40a741312ef6c04b3d20d47da27b
    )

    cursor.execute(update_query, values)

    conn.commit()

    return get_challenge(conn, challenge_id)
<<<<<<< HEAD

   

    


    

    
=======
>>>>>>> 3954c7a96d9b40a741312ef6c04b3d20d47da27b
