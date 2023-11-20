from flask import Flask, render_template
import pymongo

app = Flask(__name__)

# Connect to MongoDB
client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client['HarmonyHub']
user = db['Utenti']

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/dashboard/')
def dashboard():
    return render_template('dashboard.html')

@app.route('/signup/', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # Logic for handling signup data goes here
        pass
    return render_template('signup.html')

# Add a login route
@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Logic for handling login data goes here
        pass
    return render_template('login.html')