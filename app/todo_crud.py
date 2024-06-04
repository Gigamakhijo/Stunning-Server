import datetime
from mysql.connector.connection import MySQLConnection

from . import todo_schemas


def create_todo(conn: MySQLConnection, todo: todo_schemas.TodoCreate, user_id: int):
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
        user_id,
    )
    cursor.execute(query, values)

    conn.commit()

    return todo

def get_todo(conn: MySQLConnection, todo_id: int):
    cursor = conn.cursor()

    query = """
    SELECT date, due_date, title, contents, place, is_completed, id
    FROM todo 
    WHERE id = %s
    """

    cursor.execute(query, (todo_id,))

    todo = cursor.fetchone()

    return todo




def read_todos(
    user_id: int,
    first_date: int,
    last_date: int,
    conn: MySQLConnection,
    sort_by: str = "due_date",
):

    cursor = conn.cursor(dictionary=True)

    query = f"""
    SELECT id, date, title, contents, place, due_date, is_completed
    FROM todo
    WHERE user_id = %s
    AND date BETWEEN %s AND %s
    ORDER BY {sort_by};
    """

    last_date_max = datetime.datetime.combine(last_date, datetime.time.max)

    values = (user_id, first_date, last_date_max)

    cursor.execute(query, values)

    todos = []
    for row in cursor:
        todos.append(row)

    return todos


def update_todo(conn: MySQLConnection, todo_id: int, todo: todo_schemas.TodoUpdate):
    cursor = conn.cursor(dictionary=True)

    query = """
    SELECT id, date, title, contents, place, due_date, is_completed
    FROM todo
    WHERE user_id = %s;
    """

    cursor.execute(query)


def delete_todo(conn: MySQLConnection, todo_id: int):
    raise NotImplementedError
