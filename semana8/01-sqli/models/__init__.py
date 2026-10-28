import bcrypt


class User:

    def __init__ (self, cursor):
        self._cursor = cursor

    def login (self, username, password):
        self._cursor.execute(
            'SELECT username, password FROM users WHERE username = ?',
            (username,)
        )
        user = self._cursor.fetchone()
        if bcrypt.checkpw(password.encode('utf-8'), user[1]):
            return user
        return None


