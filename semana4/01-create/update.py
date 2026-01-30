import sqlite3


new_users = {
        'alice': 'Alice',
        'bob': 'Bobby',
        'charlie': 'Charles'
}

def update_users ():
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()

    for old_name in list(new_users.keys()):
        new_name = new_users[old_name]

        cursor.execute('UPDATE users SET name = ? WHERE name = ?', (new_name, old_name))

    conn.commit()
    conn.close()


if __name__ == '__main__':
    update_users()
