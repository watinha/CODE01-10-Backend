import sqlite3

from flask import Flask, g
from models.users import Users


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


if __name__ == '__main__':
    app.run(debug=True, port=3000, host='0.0.0.0')


