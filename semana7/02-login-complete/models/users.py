import hashlib


class Users:


    def __init__(self, cursor):
        self._cursor = cursor
        

    def login(self, username, password):
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        self._cursor.execute("SELECT * FROM users WHERE username=? AND password=?",
                             (username, hashed_password))
        user = self._cursor.fetchone()
        return user


