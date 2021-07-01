"""
This Blueprint allows for new users to register and for
users to log in and to log out of the application.
"""
from flask import Blueprint

users_blueprint = Blueprint('users', __name__, template_folder='templates')

from . import routes
