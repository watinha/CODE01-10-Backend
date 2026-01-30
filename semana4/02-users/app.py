import sqlite3

from flask import Flask
from models.users import Users


app = Flask(__name__)
conn = sqlite3.connect('db/users.db', check_same_thread=False)


@app.route('/')
def index():
    model = Users(conn.cursor())
    users = model.select_all()
    return [ { 'name': user[0] } for user in users ]


@app.route('/user/<string:name>')
def show(name):
    model = Users(conn.cursor())
    user = model.select_by_name(name)
    return { 'name': user[0], 'description': user[1], 'age': user[2] }


if __name__ == '__main__':
    app.run(debug=True, port=3000, host='0.0.0.0')


