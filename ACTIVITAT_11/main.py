from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from db_connect import get_connection
import random

app = FastAPI()

class GameInput(BaseModel):
    letter: str
    id_user: int

class GameStatus(BaseModel):
    paraula: str
    intents: int
    errors: int
    status: str

# Endpoint para agafar una paraula random


@app.get("/game/word")
def get_random_word():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT word FROM words ORDER BY RANDOM() LIMIT 1")
    word = cursor.fetchone()[0]

    cursor.close()
    conn.close()

    return {"word": word}

