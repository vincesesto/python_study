from flask import Flask, escape, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html', version='0.0.1')

@app.route('/hello/<message>')
def hello_message(message):
    return f'<h1>Welcome {(message)}!</h1>'