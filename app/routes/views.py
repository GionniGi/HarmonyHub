from app import Blueprint, render_template, current_app

# Initializing blueprints
main_blueprint = Blueprint('main', __name__)

# Home route
@main_blueprint.route('/')
def home():
    mongo = current_app.mongo
    return render_template('home.html')

@main_blueprint.route('/dashboard')
def dashboard():
    mongo = current_app.mongo
    return render_template('dashboard.html')