import datetime 
#from schemas import todo
from ..import schemas
from ..database import connect_to_mysql 
from mysql.connector import connection
import _mysql_connector

conn=connect_to_mysql()
mycursor=conn.cursor()


#connection=connection.MySQLConnection(**config)
#mysql.connector.connection.MySQLConnection

def create_todo(todo:schemas.TodoCreate,
                user_id:int):


    date=todo.date
    title=todo.title
    contents=todo.contents
    place=todo.place
    due_date=todo.due_date
    is_completed=todo.is_completed
    user_id=user_id

    insert_query="INSERT INTO todo (date DATETIME, title VARCHAR(20),contents VARCHAR(30), place VARCHAR(10), due_date DATETIME, is_completed BOOLEAN,user_id INT) VALUES (%s, %s, %s, %s, %s, %s,%s) "

    mycursor.execute(insert_query,(date, title,contents,place,due_date,is_completed,user_id))

    result=mycursor.fetchall()
    for row in result:
        print(row)
'''db_connection.commit

cursor.close()

rows=cursor.fetchall()

    for row in rows:
        last_column=row[-1]

    return last_column''''''





def get_todos_by_date(db_connection:connection.MySQLConnection, 
            user_id:int,
            date:datetime.date,
        ):

    cursor = db_connection.cursor()

    select_query="SELECT *FROM todo WHERE user_id=%s AND due_date>=%s"

    params=(user_id, date)

    cursor.execute(select_query,params)

    todos=cursor.fetchall()

    cursor.close()

    return todos 


def get_todo(db_connection:connection.MySQLConnection,
            todo_id:int):

    cursor= db_connection.cursor()
    
    select_query="SELECT * FROM todo WHERE id = %s"

    cursor.execute(select_query,(todo_id,))

    todo=cursor.fetchone()

    cursor.close()

    return todo 



def delete_todo(db_connection:connection.MySQLConnection,
                todo_id:int):

    cursor=db_connection.cursor()

    delete_query="DELETE FROM todo WHERE id= %s"

    cursor.execute(delete_query,(todo_id,))

    db_connection.commit()

    cursor.close()


def get_todos(db_connection:connect.MySQLConnection,
             date:datetime.date,
             user_id:int):'''
