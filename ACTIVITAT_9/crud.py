from db_connect import get_connection


def insert_users():
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO Users VALUES %s, %s, %s")
        conn.commit()
    finally:
        conn.close()


def read_users():
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT id, name, surname FROM Users;")
        users = cursor.fetchall()
        return users
    finally:
        conn.close()


def update_users(user_id, new_name, new_surname):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("UPDATE Users SET name = %s, surname = %s WHERE id = %s")
        conn.commit()
    finally:
        conn.close()


def delete_users(user_id):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM Users WHERE id = %s", (user_id,))
        conn.commit()
    finally:
        conn.close()

