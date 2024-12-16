import psycopg2


def get_connection():
    try:
        conn = psycopg2.connect(
            database='postgres',
            user='user_postgres',
            password='pass_postgres',
            host='localhost',
            port='5432'
        )
        return conn
    except Exception as e:
        print("Database connection error:", e)
        raise
