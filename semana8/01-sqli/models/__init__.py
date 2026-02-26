import bcrypt


class User:

    def __init__ (self, cursor):
        self._cursor = cursor

    def login (self, username, password):
        hashed_password = bcrypt.hashpw(password, bycrypt.gensalt())
        self._cursor.execute(
            'SELECT * FROM users WHERE username = ? AND password = ?',
            (username, hashed_password)
        )
        user = self._cursor.fetchone()
        if user:
            return user
        return None


