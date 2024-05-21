from mysql.connector.connection import MySQLConnection
from .. import schemas

<<<<<<< HEAD
import datetime 



def create_todo(conn: MySQLConnection, todo: schemas.TodoCreate, user_id: int):

=======
from mysql.connector.connection import MySQLConnection

from .. import schemas


def create_todo(conn: MySQLConnection, todo: schemas.TodoCreate, user_id: int):
>>>>>>> 3954c7a96d9b40a741312ef6c04b3d20d47da27b
    cursor = conn.cursor()

    query = """
    INSERT INTO todo (date, title, contents, place, due_date, is_completed, user_id)
    VALUES (%s, %s, %s, %s, %s, %s, %s);
    """

    values = (
        todo.date,
        todo.title,
        todo.contents,
        todo.place,
        todo.due_date,
        todo.is_completed,
<<<<<<< HEAD
        user_id
=======
        user_id,
>>>>>>> 3954c7a96d9b40a741312ef6c04b3d20d47da27b
    )

    cursor.execute(query, values)

    conn.commit()

    return todo


<<<<<<< HEAD
def get_todos_by_date(conn: MySQLConnection, date:datetime.date, days_left:int, first:int, amount:int, user_id: int): 

=======
def get_todos_by_date(
    conn: MySQLConnection,
    date: datetime.date,
    days_left: int,
    first: int,
    amount: int,
    user_id: int,
):
>>>>>>> 3954c7a96d9b40a741312ef6c04b3d20d47da27b
    cursor = conn.cursor(dictionary=True)

    duration = date + datetime.timedelta(days=days_left)

<<<<<<< HEAD
    #duration의 00:00:00
    duration_start = datetime.datetime.combine(duration, datetime.time.min)

    #duration의 23:59:59
    duration_end = datetime.datetime.combine(duration, datetime.time.max)
 
=======
    # duration의 00:00:00
    duration_start = datetime.datetime.combine(duration, datetime.time.min)

    # duration의 23:59:59
    duration_end = datetime.datetime.combine(duration, datetime.time.max)

>>>>>>> 3954c7a96d9b40a741312ef6c04b3d20d47da27b
    query = """
    SELECT date, due_date, title, contents, place, is_completed, id
    FROM todo
    WHERE user_id = %s
    AND due_date >= %s
    AND due_date <= %s 
    ORDER BY due_date ASC
    LIMIT %s, %s
    """
<<<<<<< HEAD
    
=======

>>>>>>> 3954c7a96d9b40a741312ef6c04b3d20d47da27b
    values = (user_id, duration_start, duration_end, first, amount)

    cursor.execute(query, values)

<<<<<<< HEAD
    todo_dict = [] #튜플의 리스트로 todo저장됨
    for row in cursor:
        todo_dict.append(row)

    return {"todos": todo_dict} #todos를 튜플의 리스트로 넣음


#여기서 todo_id는 특정 todo하나만 
def get_todo(conn: MySQLConnection, todo_id:int): 

    cursor=conn.cursor(dictionary=True)

    query="""
=======
    todo_dict = []  # 튜플의 리스트로 todo저장됨
    for row in cursor:
        todo_dict.append(row)

    return {"todos": todo_dict}  # todos를 튜플의 리스트로 넣음


# 여기서 todo_id는 특정 todo하나만
def get_todo(conn: MySQLConnection, todo_id: int):
    cursor = conn.cursor(dictionary=True)

    query = """
>>>>>>> 3954c7a96d9b40a741312ef6c04b3d20d47da27b
    SELECT date, due_date, title, contents, place, is_completed, id
    FROM todo 
    WHERE id = %s
    """

<<<<<<< HEAD
    cursor.execute(query,(todo_id,))
=======
    cursor.execute(query, (todo_id,))
>>>>>>> 3954c7a96d9b40a741312ef6c04b3d20d47da27b

    todo = cursor.fetchone()

    return todo


<<<<<<< HEAD


def update_todo(conn : MySQLConnection, todo_id : int, new_todo : schemas.TodoEdit):

    cursor = conn.cursor()

    update_query="""
=======
def update_todo(conn: MySQLConnection, todo_id: int, new_todo: schemas.TodoEdit):
    cursor = conn.cursor()

    update_query = """
>>>>>>> 3954c7a96d9b40a741312ef6c04b3d20d47da27b
    UPDATE todo
    SET date = %s, due_date = %s, title = %s, contents = %s, place = %s, is_completed = %s
    WHERE id = %s 
    """

    values = (
        new_todo.date,
        new_todo.due_date,
        new_todo.title,
        new_todo.contents,
        new_todo.place,
        new_todo.is_completed,
<<<<<<< HEAD
        todo_id

=======
        todo_id,
>>>>>>> 3954c7a96d9b40a741312ef6c04b3d20d47da27b
    )

    cursor.execute(update_query, values)

    conn.commit()
<<<<<<< HEAD

    return get_todo(conn, todo_id)
   

def delete_todo(conn: MySQLConnection, todo_id:int):
    
    cursor=conn.cursor()

    query="DELETE FROM todo WHERE id = %s"

    cursor.execute(query,(todo_id,))

    conn.commit()





    



=======

    return get_todo(conn, todo_id)


def delete_todo(conn: MySQLConnection, todo_id: int):
    cursor = conn.cursor()

    query = "DELETE FROM todo WHERE id = %s"
>>>>>>> 3954c7a96d9b40a741312ef6c04b3d20d47da27b

    cursor.execute(query, (todo_id,))

<<<<<<< HEAD
=======
    conn.commit()
>>>>>>> 3954c7a96d9b40a741312ef6c04b3d20d47da27b
