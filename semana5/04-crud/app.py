import sqlite3

from flask import Flask, request, g
from models.books import Books

app = Flask(__name__)

DATABASE = './db/app.db'

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(DATABASE)
    return g.db

@app.teardown_appcontext
def close_db(exception):
    db = g.pop('db', None)
    if db is not None:
        db.close()


@app.route('/')
def home():
    return "Welcome to the Book Library API!"


@app.route('/books', methods=['POST'])
def add_book():
    model = Books(get_db().cursor())
    json_book_data = request.get_json()
    model.add_book(
            json_book_data['title'],
            json_book_data['author']
    )
    return { "message": "Book added successfully." }, 201


@app.route('/books', methods=['GET'])
def get_books():
    model = Books(get_db().cursor())
    if request.args.get('title'):
        term = request.args.get('title')
        books = model.search(term)
    else:
        books = model.fetchall()
    return { "books": books }, 200


