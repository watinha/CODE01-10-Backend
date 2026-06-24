class Books():

    def __init__(self, conn):
        self._conn = conn

    async def add_book(self, title, author):
        await self._conn.execute(
            "INSERT INTO books (title, author) VALUES (?, ?)",
            (title, author)
        )
        await self._conn.commit()

    async def fetchall(self):
        cur = await self._conn.execute('SELECT * FROM books')
        books = await cur.fetchall()
        return self._jsonify(books)

    async def search(self, title):
        cur = await self._conn.execute('SELECT * FROM books WHERE title like ?', ('%' + title + '%',))
        books = await cur.fetchall()
        return self._jsonify(books)

    def _jsonify(self, books):
        return [ { "title": book[1], "author": book[2] } for book in books ] 


