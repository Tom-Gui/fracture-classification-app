# backend/fracture_api/api/resources.py
from flask_restx import Resource
from . import api # Import the 'api' instance from __init__.py

# Define the route for this resource within the API namespace
@api.route('/health')
class HealthCheckResource(Resource):
    def get(self):
        """Check API Health"""
        # Flask-RESTX automatically handles JSON serialization
        return {'status': 'API operational'}

# Add other resources below later