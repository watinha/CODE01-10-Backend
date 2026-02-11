import os


from flask import Flask, request


app = Flask(__name__)


@app.route('/image', methods=['POST'])
def upload_image():
    image_file = request.files['image']
    image_file.save(f'./static/images/{image_file.filename}')
    return 'Image uploaded successfully'


