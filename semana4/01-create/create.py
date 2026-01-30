import sqlite3


def create_table ():
    conn = sqlite3.connect('example.db')

    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (id INTEGER PRIMARY KEY, name TEXT)''')

    conn.commit()
    conn.close()


if __name__ == "__main__":
    create_table()
