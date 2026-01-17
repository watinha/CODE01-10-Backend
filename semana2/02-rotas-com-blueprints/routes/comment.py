from flask import Blueprint


comment_bp = Blueprint('comment', __name__)

@comment_bp.route('/')
def list_comments():
    return "Todos os comentários"

@comment_bp.route('/<int:comment_id>')
def get_comment(comment_id):
    return f"Detalhes do comentário {comment_id}"
