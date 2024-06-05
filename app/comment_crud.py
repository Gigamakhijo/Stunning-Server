import datetime
from mysql.connector.connection import MySQLConnection

from . import comment_schemas

def create_comment(conn: MySQLConnection, comment: comment_schemas.CommentCreate, user_id: int):
    cursor = conn.cursor()

    query="""
    INSERT INTO comment (date, contents, title, user_id)
    VALUES (%s, %s, %s, %s)
    """

    values = (comment.date, comment.contents, comment.title, user_id)

    cursor.execute(query, values)

    conn.commit()

    return comment


def read_comments(
    user_id: int,
    first_date: int,
    last_date: int,
    conn: MySQLConnection,
    sort_by: str = "date",
):

    cursor = conn.cursor(dictionary=True)

    last_date_max = datetime.datetime.combine(last_date, datetime.time.max)

    query = f"""
    SELECT date, title, contents, id, user_id
    FROM comment
    WHERE user_id = %s
    AND date BETWEEN %s AND %s
    ORDER BY {sort_by} ASC;
    """

    values = (user_id, first_date, last_date_max)

    cursor.execute(query, values)

    comments = []
    for row in cursor:
        comments.append(row)

    return comments



def get_comment(conn: MySQLConnection, comment_id: int):
    cursor = conn.cursor(dictionary=True)

    query = """
    SELECT id, date, contents, title, user_id 
    FROM comment 
    WHERE id = %s
    """

    cursor.execute(query, (comment_id,))

    comment = cursor.fetchone()

    return comment



def delete_comment(conn: MySQLConnection, comment_id:int):
    cursor = conn.cursor()

    query = "DELETE FROM comment WHERE id = %s"

    cursor.execute(query, (comment_id,))

    conn.commit()



def update_comment(
    conn: MySQLConnection,
    new_comment: comment_schemas.CommentEdit,
    comment_id: int
):
    cursor = conn.cursor()

    query = """
    UPDATE comment
    SET date = %s, title = %s, contents = %s
    WHERE id = %s"""

    values = (
        new_comment.date,
        new_comment.title,
        new_comment.contents,
        comment_id,
    )

    cursor.execute(query, values)

    conn.commit()

    return get_comment(conn, comment_id)
