from utils import db
import json

class Location(db.Model):
    """Model defining location with name, type, and universe"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(500), nullable=False)
    type = db.Column(db.String(500), nullable=False)
    description = db.Column(db.Text, nullable=True)
    attributes = db.Column(db.Text, nullable=True)
    universe_id = db.Column(db.Integer, db.ForeignKey('universe.id'), nullable=False)

    def init(self, data):
        self.name = data['name']
        self.description = data['description']
        self.type = data['type']
        self.attributes = json.dumps(data['attributes'])
        self.universe_id = data['universe']