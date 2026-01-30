import sqlite3


users = ['alice', 'bob', 'charlie']

def populate_database():
    conn = sqlite3.connect('example.db')
    c = conn.cursor()

    for user in users:

        c.execute("INSERT INTO users (name) VALUES (?)", (user,))

    conn.commit()
    conn.close()


if __name__ == '__main__':
    populate_database()
