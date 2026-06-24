from flask import Flask


app = Flask(__name__)


@app.route('/')
def hello ():
    return { 'message': 'Hello from Flask in WebConf 1' }


