import mysql.connector
from mysql.connector.connection import MySQLConnection

from .config import settings


def init_todo_db(conn: MySQLConnection):
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
    #cursor.execute("ALTER TABLE todo AUTO_INCREMENT = 1;")


def init_challenge_db(conn: MySQLConnection):
    cursor=conn.cursor()
    query="""
    CREATE TABLE IF NOT EXISTS challenge(
        id INT AUTO_INCREMENT PRIMARY KEY,
        date DATETIME,
        due_date DATETIME,
        title VARCHAR(20),
        is_completed BOOLEAN,
        user_id INT
    )
    """
    cursor.execute(query)


def init_comment_db(conn: MySQLConnection):
    cursor=conn.cursor()
    query="""
    CREATE TABLE IF NOT EXISTS comment(
        id INT AUTO_INCREMENT PRIMARY KEY,
        date DATETIME,
        contents VARCHAR(30),
        title VARCHAR(30),
        user_id INT
    )
    """
    cursor.execute(query)


def connect():
    conn = mysql.connector.connect(
        host=settings.mysql_host,
        user=settings.mysql_user,
        password=settings.mysql_password,
        database=settings.mysql_db
    )
    return conn


def get_conn():
    conn = connect()

    try:
        yield conn
    finally:
        conn.close()

