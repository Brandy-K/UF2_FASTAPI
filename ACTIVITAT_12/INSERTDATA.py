import psycopg2
import pandas as pd
from db_connect import get_connection


def insert_data(word):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        # Insert the word into the database
        query = "INSERT INTO words (word, language) VALUES (%s, %s)"
        cursor.execute(query, (word, "EN"))

        conn.commit()
        print(f"Inserted word: {word}")
    except Exception as e:
        print("Error inserting data:", e)
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


def csv_to_json():
    # Read the CSV file
    df = pd.read_csv("paraules_temàtica_penjat.csv")

    # Extract only the 'WORD' column
    words = df['WORD'].tolist()

    # Convert the words list to a dictionary in the format that your insert_data function expects
    return {"WORD": words}


# Get the data containing only the 'WORD' column
data = csv_to_json()

# Iterate over the list of words and insert each one into the database
for word in data["WORD"]:
    insert_data(word)
