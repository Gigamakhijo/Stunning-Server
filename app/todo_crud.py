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
    cursor = conn.cursor(dictionary=True)

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
    ORDER BY {sort_by} ASC;
    """

    last_date_max = datetime.datetime.combine(last_date, datetime.time.max)

    values = (user_id, first_date, last_date_max)

    cursor.execute(query, values)

    todos = []
    for row in cursor:
        todos.append(row)

    return todos


def update_todo(
    conn: MySQLConnection,
    new_todo: todo_schemas.TodoUpdate,
    todo_id: int,
):
    cursor = conn.cursor()

    query = """
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
        todo_id
    )

    cursor.execute(query, values)

    conn.commit()

    return get_todo(conn, todo_id)


def delete_todo(conn: MySQLConnection, todo_id: int):
    cursor = conn.cursor()

    query = "DELETE FROM todo WHERE id = %s"

    cursor.execute(query, (todo_id,))

    conn.commit()


