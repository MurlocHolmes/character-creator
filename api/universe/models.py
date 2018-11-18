from utils import db
import json

class Universe(db.Model):
    """Model to define Universe with a name, description required"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=False)
    attributes = db.Column(db.Text, nullable=True)

    def init(self, data):
        self.name = data['name']
        self.description = data['description']
        self.attributes = json.dumps(data['attributes'])