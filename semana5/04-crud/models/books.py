class Books ():

    def __init__ (self, cursor):
        self._cursor = cursor

    def add_book(self, title, author):
        self._cursor.execute('''
            INSERT INTO books (title, author)
            VALUES (?, ?)
        ''', (title, author))
        self._cursor.connection.commit()
        self._cursor.connection.close()

    def fetchall(self):
        self._cursor.execute('SELECT * FROM books')
        books = self._cursor.fetchall()
        self._cursor.connection.close()
        return self._jsonify(books)

    def search(self, title):
        self._cursor.execute('SELECT * FROM books WHERE title like ?', ('%' + title + '%',))
        books = self._cursor.fetchall()
        self._cursor.connection.close()
        return self._jsonify(books)

    def _jsonify(self, books):
        return [ { "title": book[1], "author": book[2] } for book in books ] 


