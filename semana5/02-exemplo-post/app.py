import json


from flask import Flask, request


app = Flask(__name__)


@app.route('/cars', methods=['POST'])
def create_car():
    data = request.form
    return json.dumps(data)


@app.route('/bikes', methods=['POST'])
def create_bike():
    json_data = request.get_json()
    return json.dumps(json_data)


@app.route('/trucks', methods=['POST'])
def create_truck():
    data = request.get_json() if request.is_json else request.form
    return json.dumps(data)


