from flask import Flask, render_template
from routes.user_routes import bp
import pymongo

# Initialize the app
app = Flask(__name__, static_folder='static', template_folder='view')

# Register the user blueprint
app.register_blueprint(bp, url_prefix='/user')


# Connect to MongoDB
client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client['HarmonyHub']

# Define routes
# Add a home route
@app.route('/')
def home():
    return render_template('home/home.html')

# Add a dashboard route
@app.route('/dashboard/')
def dashboard():
    return render_template('dashboard.html')