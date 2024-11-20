import psycopg2
from psycopg2 import sql


def get_db_connection():

    try:
        conn = psycopg2.connect(
            database='postgres',
            user='user_postgres',
            password='pass_postgres',
            host='localhost',
            port='5432'
        )
        return conn
    except psycopg2.Error as e:
        print("Error connecting to the database:", e)
        raise
