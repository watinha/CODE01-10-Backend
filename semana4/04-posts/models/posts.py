class Posts:


    def __init__ (self, cursor):
        self._cursor = cursor

    
    def get_posts_by_user (self, name):
        posts = self._cursor.execute("""
            SELECT posts.title, posts.content, posts.posted_at
            FROM posts 
            JOIN users ON posts.user_id = users.id 
            WHERE users.name = ?
            ORDER BY posts.posted_at DESC
        """, (name,)).fetchall()

        return posts



