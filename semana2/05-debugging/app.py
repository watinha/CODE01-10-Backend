from flask import Flask, request


app = Flask(__name__)

@app.route('/')
def hello_world():
    user = 'Willian'
    idade = 19

    idade /= 0  # This will raise a ZeroDivisionError

    return 'Hello, World!'
