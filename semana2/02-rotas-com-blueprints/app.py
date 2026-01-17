from flask import Flask
from routes.post import post_bp
from routes.comment import comment_bp


app = Flask(__name__)
app.register_blueprint(post_bp, url_prefix='/post')
app.register_blueprint(comment_bp, url_prefix='/comment')


