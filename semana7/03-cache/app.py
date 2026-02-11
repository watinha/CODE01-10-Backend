import sqlite3

from flask import Flask, g
from flask_caching import Cache

from models.posts import Posts


config = {
    "DEBUG": True,
    "CACHE_TYPE": "SimpleCache",
    "CACHE_DEFAULT_TIMEOUT": 15000
}
app = Flask(__name__)
app.config.from_mapping(config)
cache = Cache(app)


def get_connection():
    if 'db' not in g:
        g.db = sqlite3.connect('./db/posts.db')
    return g.db

@app.teardown_appcontext
def close_connection(exception):
    db = g.pop('db', None)
    if db is not None:
        db.close()


@app.route('/posts')
@cache.cached()
def get_posts():
    print('Passou aqui')
    model = Posts(get_connection().cursor())
    posts = model.get_all_posts()
    return { 'posts': posts }


