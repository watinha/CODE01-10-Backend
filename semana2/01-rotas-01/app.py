from flask import Flask


app = Flask(__name__)

@app.route('/')
def home():
    return "OK!"

@app.route('/post')
def health():
    return "Uns posts!"

@app.route('/comment')
def ready():
    return 'Uns comments!'


@app.route('/comment/<comment_id>')
def comment_detail(comment_id):
    return f'Comment com ID {comment_id}'

@app.route('/post/<int:post_id>')
def post_detail(post_id):
    return f'Post com ID {post_id}'

@app.route('/user/<str:username>/posts')
def user_posts(username):
    return f'Posts do usuário {username}'


