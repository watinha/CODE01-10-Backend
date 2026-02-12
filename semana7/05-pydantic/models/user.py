class User:


    def __init__(self, cursor):
        self._cursor = cursor


    def create(self, username, password, created_at):
        self._cursor.execute(
            "INSERT INTO users (username, password, created_at) VALUES (?, ?, ?)",
            (username, password, created_at))


    def search(self, query):
        self._cursor.execute(
            "SELECT id, username FROM users WHERE username LIKE ?",
            ('%' + query + '%',))
        return self._cursor.fetchall()


