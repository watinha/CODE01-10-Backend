import sqlite3, os, hashlib


def init_db():
    conn = sqlite3.connect(os.environ.get('DB_URL', 'db/jwt_example.db'))
    c = conn.cursor()

    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
    )''')

    username = 'watinha'
    password = hashlib.sha256('difícil'.encode()).hexdigest()

    c.execute('''
        INSERT INTO users (username, password) VALUES
            (?, ?);''', (username, password))

    conn.commit()
    conn.close()


if __name__ == '__main__':
    init_db()


