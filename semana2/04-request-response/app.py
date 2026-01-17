from flask import Flask, request


app = Flask(__name__)

@app.route('/<string:username>/<int:comment_id>')
def home(username='', comment_id=0):
    print('\n\n')
    print(f'Request Method: {request.method}')
    print(f'       Headers: \n{request.headers}')
    print(f'     view args: {request.view_args}')
    print(f'      endpoint: {request.endpoint}')
    print(f'      endpoint: {request.url_rule}')
    return "Hello, World!"

@app.route('/greetings')
def greetings():
    lang = request.headers.get('Accept-Language')
    if 'en-US' in lang:
        return 'Greetings!'
    if 'pt-BR' in lang:
        return 'Saudações!'
    else:
        return 'Saludos!'


@app.route('/text-response')
def text_response():
    return 'This is a plain text response.'

@app.route('/json-response')
def json_response():
    return { 'name': 'Flask na Pós', 'message': 'This is a JSON response com Flask.' }

@app.route('/custom')
def custom():
    return 'Custom Response', 202, { 'X-Custom-Header': 'Flask na Pós' }

@app.route('/custom2')
def custom2():
    return 'Custom 2 - Not Fount', 404, { 'Content-Language': 'en-US' }

@app.route('/custom3')
def custom3():
    return 'Custom 3 - Forbiden', 403 

