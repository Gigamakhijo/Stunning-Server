from dotenv import load_dotenv
import mysql.connector



def connect_to_mysql():
    MYSQL_HOST="localhost"
    MYSQL_USER="root"
    MYSQL_PASSWORD="0000"
    MYSQL_DB="stunning"

    conn=mysql.connector.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,

    )
    return conn
    







