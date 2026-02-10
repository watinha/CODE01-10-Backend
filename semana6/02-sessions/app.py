from flask import Flask, request, session


app = Flask(__name__)

app.secret_key = 'segredo muito importante'


@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if username == 'watinha' and password == 'difícil':
        session['username'] = username
        return { 'message': 'login bem sucedido!' }
    else:
        return { 'message': 'credenciais inválidas' }, 401


@app.route('/protected')
def protected():
    if 'username' in session and session['username'] == 'watinha':
        return { 'message': f'Bem-vindo, {session["username"]}!' }
    else:
        return { 'message': 'You shall not pass!' }, 403


