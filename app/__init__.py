from flask import Flask
from pymongo import MongoClient

def create_app():
    app = Flask(__name__)

    # Configura l'URI di MongoDB (es. 'mongodb://localhost:27017/myDatabase')
    app.config["MONGO_URI"] = "mongodb://localhost:27017/HarmonyHub"

    # Crea una connessione MongoDB
    client = MongoClient(app.config["MONGO_URI"])
    app.mongo = client.HarmonyHub


    # Importing blueprints
    from app.routes.views import main_blueprint

    return app