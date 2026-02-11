class Posts:


  def __init__(self, cursor):
    self._cursor = cursor

  def get_all_posts(self):
    self._cursor.execute("SELECT * FROM posts")
    return self._cursor.fetchall()

  def search(self, query):
    self._cursor.execute("SELECT * FROM posts WHERE title LIKE ?", ('%' + query + '%',))
    return self._cursor.fetchall()


