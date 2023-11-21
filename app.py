from flask import Flask, render_template, request
import pymongo

# Initialize the app
app = Flask(__name__)

# Connect to MongoDB
client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client['HarmonyHub']
user = db['Utenti']

# Define routes
# Add a home route
@app.route('/')
def home():
    return render_template('home.html')

# Add a dashboard route
@app.route('/dashboard/')
def dashboard():
    return render_template('dashboard.html')

# Add a login route
@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Logic for handling login data goes here
        pass
    return render_template('login.html')