from . import runs_blueprint

from flask import current_app, render_template

@runss_blueprint.route('/')
def index():
    return render_template('runs/index.html')
