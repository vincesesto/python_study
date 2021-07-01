app = Flask(__name__)

# Import the blueprints
from project.runs import runs_blueprint
from project.users import users_blueprint

# Register the blueprints
app.register_blueprint(runs_blueprint)
app.register_blueprint(users_blueprint, url_prefix='/users')
