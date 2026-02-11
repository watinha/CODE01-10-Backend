from flask import Flask, jsonify
from werkzeug.exceptions import HTTPException
from pydantic import BaseModel
from flask_pydantic import validate


app = Flask(__name__)

@app.errorhandler(Exception)
def handle_exception(e):
  return jsonify(error=str(e.description)), e.code


class UserQuery(BaseModel):
  username: str


@app.route('/user')
@validate()
def get_user(query: UserQuery):
  return f"Hello, {query.username}!"


@app.route('/error')
def error():
  b = 2/0
