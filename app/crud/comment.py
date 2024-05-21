<<<<<<< HEAD
from mysql.connector.connection import MySQLConnection
from .. import schemas

import datetime



def create_comment(conn: MySQLConnection, comment: schemas.CommentCreate, user_id: int):

    cursor=conn.cursor()

    query="""
    INSERT INTO comment (date, contents, title, user_id)
    VALUES (%s, %s, %s, %s)"""

    values=(
        comment.date,
        comment.contents,
        comment.title,
        user_id
    )
=======
import datetime

from mysql.connector.connection import MySQLConnection

from .. import schemas


def create_comment(conn: MySQLConnection, comment: schemas.CommentCreate, user_id: int):
    cursor = conn.cursor()

    query = """
    INSERT INTO comment (date, contents, title, user_id)
    VALUES (%s, %s, %s, %s)"""

    values = (comment.date, comment.contents, comment.title, user_id)
>>>>>>> 3954c7a96d9b40a741312ef6c04b3d20d47da27b

    cursor.execute(query, values)

    conn.commit()

<<<<<<< HEAD
    return comment 


def get_comment(comment_id:int, conn:MySQLConnection):

    cursor=conn.cursor(dictionary=True)

    query="""
=======
    return comment


def get_comment(comment_id: int, conn: MySQLConnection):
    cursor = conn.cursor(dictionary=True)

    query = """
>>>>>>> 3954c7a96d9b40a741312ef6c04b3d20d47da27b
    SELECT id, date, contents, title, user_id 
    FROM comment 
    WHERE id = %s
    """

<<<<<<< HEAD
    cursor.execute(query,(comment_id,))
=======
    cursor.execute(query, (comment_id,))
>>>>>>> 3954c7a96d9b40a741312ef6c04b3d20d47da27b

    comment = cursor.fetchone()

    return comment


<<<<<<< HEAD

def get_comments_by_date(first_date:datetime.date, last_date:datetime.date, first_index:int, amount:int, conn:MySQLConnection, user_id:int):

    cursor=conn.cursor(dictionary=True)

    #last_day의 23:59:59
    last_day_end = datetime.datetime.combine(last_date, datetime.time.max)

    query="""
=======
def get_comments_by_date(
    first_date: datetime.date,
    last_date: datetime.date,
    first_index: int,
    amount: int,
    conn: MySQLConnection,
    user_id: int,
):
    cursor = conn.cursor(dictionary=True)

    # last_day의 23:59:59
    last_day_end = datetime.datetime.combine(last_date, datetime.time.max)

    query = """
>>>>>>> 3954c7a96d9b40a741312ef6c04b3d20d47da27b
    SELECT date, title, contents, id, user_id
    FROM comment
    WHERE user_id = %s
    AND date >= %s AND date <= %s
    ORDER BY date ASC
    LIMIT %s, %s
    """

<<<<<<< HEAD
    values=(user_id, first_date, last_day_end, first_index, amount)

    cursor.execute(query, values)

    comment_dict=[]
    for row in cursor:
        comment_dict.append(row)

    return {"comments" : comment_dict}



def delete_comment(conn:MySQLConnection, comment_id:int):
    cursor=conn.cursor()

    delete_query="DELETE FROM comment WHERE id = %s"
=======
    values = (user_id, first_date, last_day_end, first_index, amount)

    cursor.execute(query, values)

    comment_dict = []
    for row in cursor:
        comment_dict.append(row)

    return {"comments": comment_dict}


def delete_comment(conn: MySQLConnection, comment_id: int):
    cursor = conn.cursor()

    delete_query = "DELETE FROM comment WHERE id = %s"
>>>>>>> 3954c7a96d9b40a741312ef6c04b3d20d47da27b

    cursor.execute(delete_query, (comment_id,))

    conn.commit()


<<<<<<< HEAD
def update_comment(conn:MySQLConnection, update_comment:schemas.CommentEdit, comment_id:int):
    cursor=conn.cursor()

    update_query="""
=======
def update_comment(
    conn: MySQLConnection, update_comment: schemas.CommentEdit, comment_id: int
):
    cursor = conn.cursor()

    update_query = """
>>>>>>> 3954c7a96d9b40a741312ef6c04b3d20d47da27b
    UPDATE comment
    SET date = %s, title = %s, contents = %s
    WHERE id = %s"""

<<<<<<< HEAD
    values=(
        update_comment.date,
        update_comment.title,
        update_comment.contents,
        comment_id
=======
    values = (
        update_comment.date,
        update_comment.title,
        update_comment.contents,
        comment_id,
>>>>>>> 3954c7a96d9b40a741312ef6c04b3d20d47da27b
    )

    cursor.execute(update_query, values)

    conn.commit()

    return get_comment(comment_id, conn)
<<<<<<< HEAD


    





    
=======
>>>>>>> 3954c7a96d9b40a741312ef6c04b3d20d47da27b
