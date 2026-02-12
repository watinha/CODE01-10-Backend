class Post:


    def __init__(self, cursor):
        self._cursor = cursor


    def create(self, title, content, created_at):
        self._cursor.execute(
            "INSERT INTO posts (title, content, created_at) VALUES (?, ?, ?)",
            (title, content, created_at)
        )


