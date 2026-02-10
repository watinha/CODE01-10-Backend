from flask import Flask, request
from flask_jwt_extended import JWTManager, create_access_token, jwt_required,\
                               get_jwt_identity, get_jwt


app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'Chave super secreta'
jwt = JWTManager(app)


@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username', None)
    password = request.json.get('password', None)

    if username != 'watinha' or password != 'difícil':
        return {'msg': 'You shall not pass!'}, 401

    token = create_access_token(
            identity=username, additional_claims={'role': 'admin'})
    return { 'token': token }, 200


@app.route('/protected')
@jwt_required()
def protegido():
    usuario_atual = get_jwt_identity()
    data = get_jwt()

    return { 'msg': f'Bem-vindo, {usuario_atual}! Você é {data['role']}' }, 200


