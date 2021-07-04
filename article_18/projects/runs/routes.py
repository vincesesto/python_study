from flask import Flask, render_template, request, session, redirect, url_for
from . import runs_blueprint
from flask import current_app

app = Flask(__name__)

@runs_blueprint.route('/add_run', methods=['GET', 'POST'])
def add_run():
    if request.method == 'POST':
        for key, value in request.form.items():
            print(f'{key}: {value}')

        # Save the form data to the session object
        session['type_of_run'] = request.form['type_of_run']
        session['number_of_kilometres'] = request.form['number_of_kilometres']
        session['comments'] = request.form['comments']
        return redirect(url_for('runs.list_runs'))

    return render_template('runs/add_run.html')

@runs_blueprint.route('/runs')
def list_runs():
    return render_template('runs/runs.html')
