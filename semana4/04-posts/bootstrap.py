import sqlite3

from faker import Faker


users = [
        { 'name': 'Alice', 'description': 'First user', 'age': 30 },
        { 'name': 'Bob', 'description': 'Second user', 'age': 25 },
        { 'name': 'Charlie', 'description': 'Third user', 'age': 35 },
        { 'name': 'Diana', 'description': 'Fourth user', 'age': 28 },
        { 'name': 'Eve', 'description': 'Fifth user', 'age': 22 },
]
faker = Faker()


def create_table_and_populate (users):
    conn = sqlite3.connect('db/users.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT NOT NULL,
            age INTEGER NOT NULL
        );
    ''')

    cursor.execute('''   
        CREATE TABLE IF NOT EXISTS posts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            posted_at TEXT NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users (id)
        );
    ''')

    for user in users:
        cursor.execute('''INSERT INTO users (name, description, age)
            VALUES (?, ?, ?)''', (user['name'], user['description'], user['age']))

    for i in range(0, 50):
        post = {
            'user_id': (i % len(users)) + 1,
            'title': faker.sentence(nb_words=6),
            'content': faker.paragraph(nb_sentences=3),
            'posted_at': faker.date_time_this_year().isoformat()
        }
        cursor.execute('''INSERT INTO posts (user_id, title, content, posted_at)
            VALUES (?, ?, ?, ?)''',
            (post['user_id'], post['title'], post['content'], post['posted_at']))

    conn.commit()
    conn.close()


if __name__ == '__main__':
    create_table_and_populate(users)
