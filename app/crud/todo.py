import datetime

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


def get_todos_by_date(
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
    SELECT date, due_date, title, contents, place, is_completed, id
    FROM todo
    WHERE user_id = %s
    AND due_date >= %s
    AND due_date <= %s 
    ORDER BY due_date ASC
    LIMIT %s, %s
    """

    values = (user_id, duration_start, duration_end, first, amount)

    cursor.execute(query, values)

    todo_dict = []  # 튜플의 리스트로 todo저장됨
    for row in cursor:
        todo_dict.append(row)

    return {"todos": todo_dict}  # todos를 튜플의 리스트로 넣음


# 여기서 todo_id는 특정 todo하나만
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


def update_todo(conn: MySQLConnection, todo_id: int, new_todo: schemas.TodoEdit):
    cursor = conn.cursor()

    update_query = """
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
        todo_id,
    )

    cursor.execute(update_query, values)

    conn.commit()

    return get_todo(conn, todo_id)


def delete_todo(conn: MySQLConnection, todo_id: int):
    cursor = conn.cursor()

    query = "DELETE FROM todo WHERE id = %s"

    cursor.execute(query, (todo_id,))

    conn.commit()
