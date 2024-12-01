from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import psycopg2
import random

app = FastAPI()

# Database connection
db_config = {
    "database": "postgres",
    "user": "user_postgres",
    "password": "pass_postgres",
    "host": "localhost",
    "port": "5432"
}

# Schema for response models


class ThemeSchema(BaseModel):
    option: str


class WordSchema(BaseModel):
    option: str


# Endpoint 1: Fetch all themes
@app.get("/penjat/tematica/opcions", response_model=list[ThemeSchema])
async def get_tematica_opcions():
    # fetch all themes
    try:
        conn = psycopg2.connect(**db_config)
        cur = conn.cursor()

        # Query to fetch themes
        query = "SELECT theme FROM taulapenjat;"
        cur.execute(query)

        themes = [{"option": row[0]} for row in cur.fetchall()]

        cur.close()
        conn.close()

        if not themes:
            raise HTTPException(status_code=404, detail="No themes found.")
        return themes

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Get one random word for a theme
@app.get("/penjat/tematica/{option}", response_model=WordSchema)
async def random_word_for_theme(option: str):

    try:
        conn = psycopg2.connect(**db_config)
        cur = conn.cursor()

        # Crear un query para agafar paraules del options entregat
        query = "SELECT word FROM taulapenjat WHERE theme = %s;"
        cur.execute(query, (option,))

        words = [row[0] for row in cur.fetchall()]

        cur.close()
        conn.close()

        if not words:
            raise HTTPException(status_code=404, detail="No words found for the given theme.")

        # Selecciona una paraula random using random.choice
        paraula_random = random.choice(words)
        return {"option": paraula_random}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
