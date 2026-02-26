import sqlite3, bycrypt


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
    ''', ('admin', bycrypt.hashpw('admin', bycrypt.gensalt())))

    conn.commit()
    conn.close()
