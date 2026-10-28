import sqlite3, bcrypt


def init_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
    ''')

    cursor.execute('''
        INSERT OR IGNORE INTO users (username, password) VALUES
        (?, ?)
    ''', ('admin', bcrypt.hashpw('admin'.encode('utf-8'), bcrypt.gensalt())))

    conn.commit()
    conn.close()

init_db()
