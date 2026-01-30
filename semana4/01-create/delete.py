import sqlite3


ids = list(range(1, 4))

def delete_users ():
    conn = sqlite3.connect('example.db')
    c = conn.cursor()

    for id in ids:
        c.execute('DELETE FROM users WHERE id = ?', (id,))

    conn.commit()
    conn.close()

if __name__ == '__main__':
    delete_users()


