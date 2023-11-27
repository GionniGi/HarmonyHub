from flask import Flask, render_template
from routes.user import user_blueprint
import pymongo

# Initialize the app
app = Flask(__name__, template_folder='view/templates')

app.register_blueprint(user_blueprint, url_prefix='/user')


# Connect to MongoDB
client = pymongo.MongoClient('mongodb://localhost:27017/')
# Create database and collection
db = client['HarmonyHub']
users = db['Users']

# Define routes
# Add a home route
@app.route('/')
def home():
    return render_template('home.html')

# Add a dashboard route
@app.route('/dashboard/')
def dashboard():
    return render_template('dashboard.html')