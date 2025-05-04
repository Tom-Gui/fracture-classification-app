# backend/fracture_api/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from config import Config
import os

# Initialize extensions without app instances
db = SQLAlchemy()
migrate = Migrate()
cors = CORS()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize extensions with app instance
    db.init_app(app)
    migrate.init_app(app, db)
    # Basic CORS for development
    cors.init_app(app, resources={r"/api/*": {"origins": "*"}})

    # Register Blueprints here (in later steps)
    # --- Register Blueprints ---
    from .api import bp as api_blueprint # Import the blueprint
    # All routes in api_blueprint will be prefixed with /api/v1
    app.register_blueprint(api_blueprint, url_prefix='/api/v1')
    # --- End Register Blueprints ---

    # Add a simple test route
    @app.route('/health')
    def health_check():
        return "Backend OK", 200

    return app
