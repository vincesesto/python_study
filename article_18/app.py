from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)

app.secret_key = '\x98)\x861hX[\xf1\xc5Z\xd5SSe@\xe7[K\xfe\xb5\xc7~\xb0\x99\x1e\x8f\xfem\xa6F\xc1&'

# Import the blueprints
from projects.runs import runs_blueprint
from projects.users import users_blueprint

# Register the blueprints
app.register_blueprint(runs_blueprint)
app.register_blueprint(users_blueprint, url_prefix='/users')
