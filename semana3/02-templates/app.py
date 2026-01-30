from flask import Flask, render_template, url_for


app = Flask(__name__)

@app.route('/')
def hello_world_com_templates ():
    return render_template('hello_world.html')

@app.route('/about')
def about():
    username = 'John Doe'
    age = 30
    products = ['Laptop', 'Smartphone', 'Tablet']
    return render_template('about.html', username=username,
                           age=age, products=products)


@app.route('/about-with-css')
def about2():
    home_url = url_for('hello_world_com_templates')
    image_url = url_for('static', filename='flask.png')
    css_url = url_for('static', filename='main.css')
    js_url = url_for('static', filename='main.js')
    return render_template('about2.html', 
                           home_url=home_url,
                           image_url=image_url,
                           css_url=css_url,
                           js_url=js_url)


