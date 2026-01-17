from flask import Blueprint


post_bp = Blueprint('post', __name__)

@post_bp.route('/')
def list_posts():
    return "Todas as postagens"

@post_bp.route('/<int:post_id>')
def get_post(post_id):
    return f"Detalhes da postagem {post_id}"
