import os, hashlib, sqlite3

from flask import Flask, request, g
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity, get_jwt

from models.users import Users


app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY', 'super secreta')
jwt = JWTManager(app)

def get_connection ():
    if 'conn' not in g:
        g.conn = sqlite3.connect(os.environ.get('DB_URL', 'db/jwt_example.db'))
    return g.conn

@app.teardown_appcontext
def close_connection(exception):
    conn = g.pop('conn', None)
    if conn is not None:
        conn.close()


@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')

    model = Users(get_connection().cursor())
    user = model.login(username, password)

    if user:
        token = create_access_token(identity=username)
        return { 'token': token } 
    else:
        return { 'error': 'Invalid credentials' }, 401


@app.route('/protected')
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return { 'logged_in_as': current_user }


