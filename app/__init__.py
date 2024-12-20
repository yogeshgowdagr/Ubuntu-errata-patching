from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.routes import init_routes
import os

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    # Create database if it doesn't exist
    if not os.path.exists("app.db"):
        with app.app_context():
            db.create_all()
            print("Database created!")

    init_routes(app)

    return app
