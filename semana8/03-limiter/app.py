from flask import Flask
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address


app = Flask(__name__)
limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["200 per day", "2 per hour"]
)

@app.route("/")
def index():
    return { "message": "Hello, World!" }


