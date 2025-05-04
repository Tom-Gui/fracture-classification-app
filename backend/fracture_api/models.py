# backend/fracture_api/models.py
from . import db
import datetime


class TestModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    # TODO Replace deprecated ".utcnow" method
    timestamp = db.Column(db.DateTime, index=True, default=datetime.datetime.utcnow)

    def __repr__(self):
        return f'<TestModel {self.name}>'

# You might later replace/add models relevant to fracture classification, e.g.:
# class ClassificationLog(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     input_data = db.Column(db.JSON) # Store input JSON
#     output_guidelines = db.Column(db.Text)
#     timestamp = db.Column(db.DateTime, index=True, default=datetime.datetime.utcnow)