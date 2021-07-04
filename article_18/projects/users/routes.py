from flask import Flask, render_template, request, session, redirect, url_for, flash
from . import users_blueprint

app = Flask(__name__)

@users_blueprint.route('/')
def index():
    return render_template('users/index.html')

@users_blueprint.route('/about')
def about():
    return render_template('users/about.html', version='0.0.1')
