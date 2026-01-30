import sqlite3


class Users ():


    def __init__(self, cursor=None):
        self._cursor = cursor

    
    def select_all (self):
        self._cursor.execute('SELECT name FROM users')
        return self._cursor.fetchall()


    def select_by_name (self, name):
        self._cursor.execute('SELECT name, description, age FROM users WHERE name = ?', (name,))
        return self._cursor.fetchone()


