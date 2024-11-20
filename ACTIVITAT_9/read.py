from connection import get_db_connection
import users


def read():
    conn = get_db_connection()
    try:
        cur = conn.cursor()
        cur.execute("SELECT id, name, surname FROM users")
        users = cur.fetchall()
        return users
    finally:
        cur.close()
        conn.close()