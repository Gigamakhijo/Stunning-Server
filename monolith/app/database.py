import mysql.connector
from mysql.connector.connection import MySQLConnection

from .config import settings


def init_db(conn: MySQLConnection):
    cursor = conn.cursor()
    query = """
    CREATE TABLE IF NOT EXISTS todo (
        id INT AUTO_INCREMENT PRIMARY KEY,
        date DATETIME,
        title VARCHAR(20),
        contents VARCHAR(30),
        place VARCHAR(30),
        due_date DATETIME,
        is_completed BOOLEAN,
        user_id INT
    )
    """
    cursor.execute(query)


def connect():
    conn = mysql.connector.connect(
        host=settings.mysql_host,
        user=settings.mysql_user,
        password=settings.mysql_password,
        database=settings.mysql_db,
    )
    return conn


def get_conn():
    conn = connect()

    try:
        yield conn
    finally:
        conn.close()
