import sqlite3, logging

from flask import Flask, jsonify, g, request
from werkzeug.exceptions import HTTPException
from pydantic import BaseModel
from flask_pydantic import validate


app = Flask(__name__)
app.logger.setLevel(logging.INFO)


@app.errorhandler(Exception)
def handle_exception(e):
  app.logger.error(f"An error occurred: {str(e)}")
  return jsonify(error=str(e.description)), e.code

def get_db():
    if 'db' not in g:
        app.logger.info("Connecting to the database...")
        g.db = sqlite3.connect('database.db')
        cursor = g.db.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL
            )
        ''')
    return g.db

@app.teardown_appcontext
def close_db(exception):
    db = g.pop('db', None)
    if db is not None:
        app.logger.info("Disconnecting the database...")
        db.close()

class Users:

    def __init__ (self, cursor):
        self._cursor = cursor

    def add(self, name):
        self._cursor.execute('INSERT INTO users (name) VALUES (?)', (name,))
        return self._cursor.lastrowid

    def get_all(self):
        self._cursor.execute('SELECT id, name FROM users')
        return self._cursor.fetchall()


@app.route('/users', methods=['POST'])
def add_user():
    model = Users(get_db().cursor())
    app.logger.info("Adding a new user...")
    model.add(request.get_json().get('name'))
    return jsonify(message='User added successfully'), 201

@app.route('/users', methods=['GET'])
def get_users():
    model = Users(get_db().cursor())
    users = model.get_all()
    app.logger.info("Retrieving users...")
    return jsonify(users=[{'id': user[0], 'name': user[1]} for user in users]), 200


