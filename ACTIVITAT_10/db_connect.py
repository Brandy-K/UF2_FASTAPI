import psycopg2


def insert_data(pos, data):
    try:
        conn = psycopg2.connect(
            database='postgres',
            user='user_postgres',
            password='pass_postgres',
            host='localhost',
            port='5432'
        )

        cur = conn.cursor()

        sql = "INSERT INTO taulapenjat (word, theme) VALUES (%s, %s);"

        word = data.get("WORD")[pos]
        theme = data.get("THEME")[pos]
        values = (word, theme)

        # Execute query
        cur.execute(sql, values)

        # Commit
        conn.commit()

        return {"Message": "Data inserted successfully!"}

    except Exception as e:
        return {"Error": str(e)}

    finally:

        if cur:
            cur.close()
        if conn:
            conn.close()
