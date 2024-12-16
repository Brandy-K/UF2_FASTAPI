from db_connect import get_connection

def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    # Your SQL queries for creating tables
    queries = [
        '''
CREATE TABLE IF NOT EXISTS users (
    id_user SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL
);

        ''',
        '''
        CREATE TABLE words (
            id_word SERIAL PRIMARY KEY,
            word VARCHAR(50) NOT NULL,
            language VARCHAR(20) DEFAULT 'EN',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        ''',
        '''
        CREATE TABLE registre_joc (
            id_partida SERIAL PRIMARY KEY,
            id_user INT NOT NULL,
            id_word INT NOT NULL,
            intents INT DEFAULT 0,
            errors INT DEFAULT 0,
            total_partida INT,
            punts_partida_actual INT,
            partides_guanyades INT,
            partida_amb_mes_punts TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (id_user) REFERENCES users(id_user),
            FOREIGN KEY (id_word) REFERENCES words(id_word)
        );
        ''',

        '''
        CREATE TABLE letters (
            id_letter SERIAL PRIMARY KEY,
            letter CHAR(1) NOT NULL,
            language VARCHAR(20) DEFAULT 'EN',
            is_available BOOLEAN DEFAULT TRUE,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        '''
    ]

    # Execute each query
    for query in queries:
        cursor.execute(query)

    conn.commit()
    cursor.close()
    conn.close()

if __name__ == "__main__":
    create_tables()
