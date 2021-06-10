from flask import Flask, render_template, request, session, redirect, url_for

app.secret_key = '\x98)\x861hX[\xf1\xc5Z\xd5SSe@\xe7[K\xfe\xb5\xc7~\xb0\x99\x1e\x8f\xfem\xa6F\xc1&'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html', version='0.0.1')

@app.route('/hello/<message>')
def hello_message(message):
    return f'<h1>Welcome {(message)}!</h1>'

@app.route('/add_run', methods=['GET', 'POST'])
def add_run():
    if request.method == 'POST':
        for key, value in request.form.items():
            print(f'{key}: {value}')

        # Save the form data to the session object
        session['type_of_run'] = request.form['type_of_run']
        session['number_of_kilometres'] = request.form['number_of_kilometres']
        session['comments'] = request.form['comments']
        return redirect(url_for('list_runs'))

    return render_template('add_run.html')

@app.route('/runs/')
def list_runs():
    return render_template('runs.html')