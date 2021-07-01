"""
This blueprint allows for users to add, edit, and delete
run data from their application.
"""
from flask import Blueprint

stocks_blueprint = Blueprint('runs', __name__, template_folder='templates')

from . import routes
