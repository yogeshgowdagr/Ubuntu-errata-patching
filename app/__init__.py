from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.routes import init_routes
from app.models import db
from config import config

# Initialize the database
db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    # Initialize the database
    db.init_app(app)

    # Import and register blueprints
    from .routes import init_routes
    init_routes(app)

    # Import models to ensure they are registered with SQLAlchemy
    from . import models

    return app