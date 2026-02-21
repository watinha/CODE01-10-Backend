import bleach, sqlite3

from datetime import datetime
from flask import Flask, g
from pydantic import BaseModel, field_validator
from flask_pydantic import validate
from models.posts import Post


app = Flask(__name__)


def get_conn():
    if "conn" not in g:
        g.conn = sqlite3.connect("./db/database.db")
    return g.conn

@app.teardown_appcontext
def close_conn(exception):
    conn = g.pop("conn", None)
    if conn is not None:
        conn.close()


class PostParams(BaseModel):
    title: str
    content: str
    created_at: datetime

    @field_validator("content")
    @classmethod
    def sanitize_content(cls, value):
        return bleach.clean(value)


@app.route("/post", methods=["POST"])
@validate()
def create_user(params: PostParams):
    # cria o post sem tags de XSS
    print(PostParams)
    model = Post(get_conn().cursor())
    # impede SQL Inject
    model.create(params.title, params.content, params.created_at)


