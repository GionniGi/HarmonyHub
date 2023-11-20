from flask import Flask
from pymongo import MongoClient

def create_app():
    app = Flask(__name__)

    # Configura l'URI di MongoDB (es. 'mongodb://localhost:27017/myDatabase')
    app.config["MONGO_URI"] = "mongodb://localhost:27017/HarmonyHub"

    # Crea una connessione MongoDB
    client = MongoClient(app.config["MONGO_URI"])
    app.mongo = client.HarmonyHub

    # Importazione delle blueprint delle route
    from .routes.views import main_blueprint
    app.register_blueprint(main_blueprint)

    return app