from flask import Flask


app = Flask(__name__)

@app.route("/hello")
def hello():
    return { "message": "Hello, World!" }


if __name__ == "__main__":
  app.run(debug=True, port=3000, host='0.0.0.0')


