from mysql.connector.connection import MySQLConnection

from .. import schemas


def create_todo(conn: MySQLConnection, todo: schemas.TodoCreate, user_id: int):
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


def get_todo(conn: MySQLConnection, user_id: int):
    cursor = conn.cursor(dictionary=True)
    query = """
    SELECT id, date, title, contents, place, due_date, is_completed
    FROM todo
    WHERE user_id = %s;
    """
    values = (user_id,)
    cursor.execute(query, values)

    todos = []
    for row in cursor:
        todos.append(row)

    return {"todos": todos}
