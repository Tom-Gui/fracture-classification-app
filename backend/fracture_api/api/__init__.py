# backend/fracture_api/api/__init__.py
from flask import Blueprint
from flask_restx import Api

# Create the Blueprint instance
# First argument ('api'): endpoint name for url_for()
# Second argument (__name__): import name
# Third argument (not specified): URL prefix for routes within this blueprint
bp = Blueprint('api', __name__)

# Initialize Flask-RESTX Api with the blueprint
# Add metadata for Swagger documentation
api = Api(
    bp,
    version='1.0',
    title='Fracture Classification API',
    description='API for classifying fractures based on input parameters.',
    doc='/doc/' # Optional: path for Swagger UI documentation
)

# Import resources AFTER initializing 'api' to avoid circular imports
from . import resources