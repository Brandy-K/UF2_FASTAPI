from fastapi import FastAPI, HTTPException
from db_connect import get_connection
from pydantic import BaseModel
app = FastAPI()


class UserInfo(BaseModel):
    id_user: int
    username: str
    email: str
# Endpoint to Create a new user


@app.post("/users")
def create_user(user: UserInfo):
    conn = get_connection()
    cursor = conn.cursor()

    # Insert the user
    cursor.execute("""
        INSERT INTO users (id_user, username, email)
        VALUES (%s, %s, %s)
    """, (user.id_user, user.username, user.email))

    conn.commit()
    cursor.close()
    conn.close()

    return {"message": "User Inserted Successfully"}

# Endpoint to Read a user


@app.get("/users/{id_user}")
def read_all_users(id_user: int):

    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM users where id_user = %s", (id_user,))
        users = cursor.fetchone()
        conn.commit()
    finally:
        cursor.close()
        conn.close()
    return {"users": users}

# Endpoint to Update a user


@app.put("/users/")
def update_users(id_user: int, username: str):

    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("UPDATE users SET username = %s where id_user = %s", (username, id_user))
        conn.commit()
    finally:
        cursor.close()
        conn.close()
    return {"message": "user updated succesfully"}
# Endpoint to Delete a user


@app.delete("/users/")
def delete_users(id_user: int):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        # Per eliminar un usuari de la taula d'usuaris, primer heu d'eliminar tots els registres de la taula
        # registre_joc on es fa referència a id_user. Si intenteu suprimir l'usuari sense eliminar aquests registres
        # dependents, la base de dades generarà un error de restricció de clau estrangera.
        cursor.execute("DELETE FROM registre_joc WHERE id_user = %s", (id_user,))

        # Delete the user
        cursor.execute("DELETE FROM users WHERE id_user = %s", (id_user,))

        conn.commit()
    except Exception as e:

        return {"error": f"Failed to delete user: {str(e)}"}
    finally:
        cursor.close()
        conn.close()
    return {"message": "User deleted successfully"}

# Endpoint to Create a word


# Endpoint to Read a word


# Endpoint to Update a word


# Endpoint to Delete a word

# Endpoint to Create registre_joc


# Endpoint to Read a registre


# Endpoint to Update a registre

# Endpoint to Delete a registre
