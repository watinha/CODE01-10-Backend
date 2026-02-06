import json


from flask import Flask, request


app = Flask(__name__)


@app.route('/product')
def product():
    product_id = request.args.get('id', 'unknown')
    return f"Product Page for Product ID: {product_id}"


@app.route('/comments')
def comments():
    return json.dumps(request.args)


@app.route('/order', methods=['GET'])
def orders():
    return f'O pedido saiu {request.args.get('status', 'pendente')}'


