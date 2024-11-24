from db_connect import get_connection


def insert_users():
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO users (name, surname) VALUES (%s, %s)", ("Brandy", "Kisia"))
        cursor.execute("INSERT INTO users (name, surname) VALUES (%s, %s)", ("Doua", "Alabed"))
        conn.commit()
    finally:
        conn.close()


def read_users():
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT id, name, surname FROM users;")
        users = cursor.fetchall()
        return users
    finally:
        conn.close()


def update_users(Id, name, surname):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("UPDATE users SET name = %s, surname = %s WHERE id = %s", (name, surname, Id))
        conn.commit()
    finally:
        conn.close()


def delete_users(Id):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM Users WHERE id = %s", (Id,))
        conn.commit()
    finally:
        conn.close()

