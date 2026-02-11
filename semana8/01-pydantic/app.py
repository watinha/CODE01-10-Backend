import sqlite3


from flask import Flask, request, g
from pydantic import BaseModel
from flask_pydantic import validate

from models.user import User
from pydantic_models.user import UserQuery, UserCreate


app = Flask(__name__)

def get_connection():
    if 'db' not in g:
        g.db = sqlite3.connect('./db/database.db')
    return g.db

@app.teardown_appcontext
def close_connection(exception):
    db = g.pop('db', None)
    if db is not None:
        db.close()


@app.route('/users', methods=['GET'])
@validate()
def get_users(query: UserQuery):
    model = User(get_connection().cursor())
    users = model.search(query.username)
    return { 'users': users }


@app.route('/users', methods=['POST'])
@validate()
def create_user(body: UserCreate):
    model = User(get_connection().cursor())
    user_id = model.create(body.username, body.password, body.created_at)
    return { 'user_id': user_id }


