import psycopg2
import csv
from db_connect import get_connection

# File path to your CSV
csv_file = 'paraules_temàtica_penjat.csv'

try:
    # Connect to the database
    conn = get_connection()
    cursor = conn.cursor()

    with open(csv_file, mode="r", encoding="utf-8") as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            print(row)  # Print each row to understand the structure

    # Open the CSV file
    dict_list = []
    with open(csv_file, mode="r") as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        for rows in csv_reader:
            dict_list.append({'WORD': rows[0], 'THEME': rows[1]})

        # Insert data row by row
        for item in dict_list:
            sql = "INSERT INTO taulapenjat(word, theme) VALUES (%s, %s)"
            val = item['WORD'], item['THEME']
            cursor.execute(sql, val)

    # Commit changes
    conn.commit()
    print("Data added successfully!")

except Exception as e:
    print("Error:", e)

finally:
    # Close the database connection
    if conn:
        cursor.close()
        conn.close()
