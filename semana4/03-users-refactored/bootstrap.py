import sqlite3


users = [
        { 'name': 'Alice', 'description': 'First user', 'age': 30 },
        { 'name': 'Bob', 'description': 'Second user', 'age': 25 },
        { 'name': 'Charlie', 'description': 'Third user', 'age': 35 },
        { 'name': 'Diana', 'description': 'Fourth user', 'age': 28 },
        { 'name': 'Eve', 'description': 'Fifth user', 'age': 22 },
]


def create_table_and_populate (users):
    conn = sqlite3.connect('db/users.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT NOT NULL,
            age INTEGER NOT NULL
        )
    ''')


    for user in users:
        cursor.execute('''INSERT INTO users (name, description, age)
            VALUES (?, ?, ?)''', (user['name'], user['description'], user['age']))



    conn.commit()
    conn.close()


if __name__ == '__main__':
    create_table_and_populate(users)
