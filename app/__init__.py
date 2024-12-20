from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.routes import init_routes
from app.models import db

# Initialize the database
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    # Initialize the database
    db.init_app(app)

    # Initialize routes
    init_routes(app)

    return app
