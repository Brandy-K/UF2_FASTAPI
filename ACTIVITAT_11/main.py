from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from db_connect import get_connection
import random

app = FastAPI()

class GameInput(BaseModel):
    id_user: int
    username: str
    email: str

class GameGuess(BaseModel):
    id_partida: int
    id_user: int
    letter: str

class GameStatus(BaseModel):
    paraula: str
    intents: int
    errors: int
    status: str

def get_word_by_id(word_id, cursor):
    cursor.execute("SELECT word FROM words WHERE id_word = %s", (word_id,))
    word = cursor.fetchone()[0]  # Retrieve the word from the database
    return word

# 1. Start a new game - Select a random word
@app.post("/game/start")
def start_game(user: GameInput):
    conn = get_connection()
    cursor = conn.cursor()

    # Insert the user if they do not exist
    cursor.execute("""
        INSERT INTO users (id_user, username, email)
        VALUES (%s, %s, %s)
        ON CONFLICT (id_user) DO NOTHING
    """, (user.id_user, user.username, user.email))

    # Insert a new game record into the registre_joc table
    cursor.execute("""
        INSERT INTO registre_joc (id_user, id_word)
        VALUES (%s, (SELECT id_word FROM words ORDER BY RANDOM() LIMIT 1))
    """, (user.id_user,))

    conn.commit()
    cursor.close()
    conn.close()

    return {"message": "Game started successfully"}

# 2. Make a guess - Increment attempts and errors
@app.post("/game/guess")
def make_guess(guess: GameGuess):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id_partida, id_word, errors, intents
        FROM registre_joc
        WHERE id_partida = %s AND id_user = %s
    """, (guess.id_partida, guess.id_user))

    game = cursor.fetchone()

    if not game:
        cursor.close()
        conn.close()
        raise HTTPException(status_code=404, detail="Game not found")

    word = get_word_by_id(game[1], cursor)

    # Increment intents (number of guesses)
    cursor.execute("""
        UPDATE registre_joc
        SET intents = intents + 1
        WHERE id_partida = %s
    """, (guess.id_partida,))

    # Check if the guessed letter is in the word
    if guess.letter not in word:
        cursor.execute("""
            UPDATE registre_joc
            SET errors = errors + 1
            WHERE id_partida = %s
        """, (guess.id_partida,))

    conn.commit()
    cursor.close()
    conn.close()

    return {"status": "guess recorded"}

# 3. Retrieve a random word from the words table
@app.get("/game/word")
def get_random_word():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT word FROM words ORDER BY RANDOM() LIMIT 1")
    word = cursor.fetchone()[0]

    cursor.close()
    conn.close()

    return {"word": word}

# 4. Get the letters of the alphabet (including extended characters like ñ, ç)
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

# 5. Get the player stats - total games, games won, current points, etc.
@app.get("/game/stats")
def get_player_stats(id_user: int):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT total_partida, partides_guanyades, punts_partida_actual, partida_amb_mes_punts
        FROM registre_joc
        WHERE id_user = %s
    """, (id_user,))

    stats = cursor.fetchone()

    if not stats:
        cursor.close()
        conn.close()
        raise HTTPException(status_code=404, detail="Player not found")

    cursor.close()
    conn.close()

    return {
        "total_partides": stats[0],
        "partides_guanyades": stats[1],
        "punts_partida_actual": stats[2],
        "partida_amb_mes_punts": stats[3]
    }
