import sqlite3

from flask import Flask, g
from models.users import Users
from models.posts import Posts


app = Flask(__name__)


def get_connection ():
    if 'db' not in g:
        g.db = sqlite3.connect('db/users.db')
    return g.db

@app.teardown_appcontext
def close_connection(exception):
    db = g.pop('db', None)
    if db is not None:
        db.close()


@app.route('/')
def index():
    model = Users(get_connection().cursor())
    users = model.select_all()
    return [ { 'name': user[0] } for user in users ]


@app.route('/user/<string:name>')
def show(name):
    model = Users(get_connection().cursor())
    user = model.select_by_name(name)
    return { 'name': user[0], 'description': user[1], 'age': user[2] }


@app.route('/user/<string:name>/posts')
def get_posts (name):
    posts_model = Posts(get_connection().cursor())
    posts = posts_model.get_posts_by_user(name)
    return [
            { 
              'title': post[0],
              'content': post[1],
              'posted_at': post[2]
            } for post in posts ]


if __name__ == '__main__':
    app.run(debug=True, port=3000, host='0.0.0.0')


