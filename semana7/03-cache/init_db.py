import sqlite3

from faker import Faker


faker = Faker()


def create_table_and_populate ():
    conn = sqlite3.connect('db/posts.db')
    cursor = conn.cursor()

    cursor.execute('''   
        CREATE TABLE IF NOT EXISTS posts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            posted_at TEXT NOT NULL
        );
    ''')

    for i in range(0, 50):
        post = {
            'title': faker.sentence(nb_words=6),
            'content': faker.paragraph(nb_sentences=3),
            'posted_at': faker.date_time_this_year().isoformat()
        }
        cursor.execute('''INSERT INTO posts (title, content, posted_at)
            VALUES (?, ?, ?)''',
        (post['title'], post['content'], post['posted_at']))

    conn.commit()
    conn.close()


if __name__ == '__main__':
    create_table_and_populate()


