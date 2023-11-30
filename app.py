from flask import Flask, render_template
from flask_jwt_extended import JWTManager, jwt_required
from routes.user_routes import bp
import pymongo, datetime

# Initialize the app
app = Flask(__name__, template_folder='view')

# Configure jwt
jwt = JWTManager(app)
app.config['JWT_SECRET_KEY'] = 'secret'
app.config['JWT_TOKEN_EXPIRES'] = datetime.timedelta(days=1)

# Register the user blueprint
app.register_blueprint(bp, url_prefix='/user')

# Connect to MongoDB
client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client['HarmonyHub']

# Add a home route
@app.route('/')
def home():
    return render_template('home/home.html')

# Add a dashboard route
@app.route('/dashboard/')
@jwt_required
def dashboard():
    return render_template('dashboard.html')