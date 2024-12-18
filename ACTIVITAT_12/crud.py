from fastapi import FastAPI,HTTPException
from db_connect import get_connection
from pydantic import BaseModel
from datetime import datetime
app = FastAPI()


class UserInfo(BaseModel):
    id_user: int
    username: str
    email: str


class gamewords(BaseModel):
    id_word: int
    word: str
    language: str


class registreJoc(BaseModel):
    id_user: int  # Foreign key to users table
    id_word: int  # Foreign key to words table
    intents: int = 0
    errors: int = 0
    total_partida: int = 0
    punts_partida_actual: int = 0
    partides_guanyades: int = 0
    partida_amb_mes_punts: int = 0


class Letters(BaseModel):
    id_letter: int
    letter: str
    is_available: bool
    created_at = datetime.utcnow()

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
@app.get("/words/{id_word}")
def read_all_words(id_word: int):

    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM words where id_word = %s", (id_word,))
        words = cursor.fetchall()
    finally:
        cursor.close()
        conn.close()
    return {"words": words}


# Endpoint to Update a word
@app.put("/words/{id_word}")
def update_words(id_word: int, word: str):

    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("UPDATE words SET username = %s where id_word = %s", (word, id_word,))
        conn.commit()
    finally:
        cursor.close()
        conn.close()
    return {"message": "user updated succesfully"}

# Endpoint to Delete a word


@app.delete("/words/")
def delete_users(id_word: int):
    conn = get_connection()
    cursor = conn.cursor()
    try:

        # Delete the word
        cursor.execute("DELETE FROM words WHERE id_user = %s", (id_word,))

        conn.commit()
    except Exception as e:

        return {"error": f"Failed to delete word: {str(e)}"}
    finally:
        cursor.close()
        conn.close()
    return {"message": "Word deleted successfully"}
# Endpoint to Create registre_joc


# Endpoint to Read a registre
@app.get("/games/")
def read_all_games():

    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM registre_joc")
        games = cursor.fetchall()
    finally:
        cursor.close()
        conn.close()
    return {"games": games}

# Endpoint to Update a registre


@app.put("/registre/{id_partida}")
def update_registre(id_partida: int, errors: int):

    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("UPDATE registre_joc SET errors = %s where id_partida = %s", (errors, id_partida,))
        conn.commit()
    finally:
        cursor.close()
        conn.close()
    return {"message": "registre updated succesfully"}


# Endpoint to Delete a registre
@app.delete("/registre/")
def delete_registre(id_partida: int):
    conn = get_connection()
    cursor = conn.cursor()
    try:

        # Delete the word
        cursor.execute("DELETE FROM registre_joc WHERE id_user = %s", (id_partida,))

        conn.commit()
    except Exception as e:

        return {"error": f"Failed to delete registre: {str(e)}"}
    finally:
        cursor.close()
        conn.close()
    return {"message": "registre deleted successfully"}
# Endpoint to insert letter


@app.post("/letters/")
def insert_letter(letter: Letters):
    conn = get_connection()
    cursor = conn.cursor()

    # Insert the letter
    cursor.execute("""
        INSERT INTO letters (id_letter, letter, is_available, created_at)
        VALUES (%s, %s, %s, %s)
    """, (letter.id_letter, letter.letter, letter.is_available, letter.created_at))

    conn.commit()
    cursor.close()
    conn.close()

    return {"message": "Letter Inserted Successfully"}


# Endpoint to read letters


@app.get("/game/letters")
def get_letters():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT letter FROM letters WHERE is_available = TRUE")
    letters = cursor.fetchall()

    available_letters = [letter[0] for letter in letters]

    cursor.close()
    conn.close()

    return {"letters": available_letters}

# Endpoint to delete letter


@app.delete("/letters/")
def delete_letter(id_letter: int):
    conn = get_connection()
    cursor = conn.cursor()
    try:

        # Delete the letter
        cursor.execute("DELETE FROM letters WHERE id_letter = %s", (id_letter,))

        conn.commit()
    except Exception as e:

        return {"error": f"Failed to delete letter: {str(e)}"}
    finally:
        cursor.close()
        conn.close()
    return {"message": "Letter deleted successfully"}

