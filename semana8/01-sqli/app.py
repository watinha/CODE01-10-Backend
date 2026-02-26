import sqlite3


from flask import Flask, g, request
from flask_jwt_extended import JWTManager, create_access_token, jwt_required,\
                               get_jwt_identity, get_jwt
from models import User


app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'Chave super secreta'
jwt = JWTManager(app)


app = Flask(__name__)


def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect('database.db')
    return g.db


@app.teardown_appcontext
def close_db(exception):
    db = g.pop('db', None)
    if db is not None:
        db.close()


@app.route('/login')
def login():
    username = request.args.get('username')
    password = request.args.get('password')

    model = User(get_db().cursor())
    user = model.login(username, password)

    if user is None:
        return {'msg': 'You shall not pass!'}, 401

    token = create_access_token(
            identity=username, additional_claims={'role': 'admin'})

    return { 'token': token }, 200

    return user


