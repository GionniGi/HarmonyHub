from flask import Flask
from pymongo import MongoClient

# Initialize MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['HarmonyHub']

# Initialize the app
app = Flask(__name__)