import sqlite3


def init_db():
    conn = sqlite3.connect('db/database.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS posts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            created_at TEXT NOT NULL
        )
    ''')

    conn.commit()
    conn.close()


if __name__ == "__main__":
    init_db()


