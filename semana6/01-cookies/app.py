from flask import Flask, make_response, request


app = Flask(__name__)


@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    if username == 'watinha' and password == 'difícil':
        response = make_response({ 'message': 'Login successful!' })
        response.set_cookie('username', username)
        return response
    else:
        return 'Invalid credentials', 401


@app.route('/protected')
def protected():
    username = request.cookies.get('username')
    if username == 'watinha':
        return f'Welcome, {username}! This is a protected page.'
    else:
        return 'You shall not pass!', 401


