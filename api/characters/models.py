from utils import db
import json

class Character(db.Model):
    """Model defining Character with name and universe"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(500), nullable=False)
    description = db.Column(db.Text, nullable=False)
    attributes = db.Column(db.Text, nullable=False)
    universe_id = db.Column(db.Integer, db.ForeignKey('universe.id'), nullable=False)

    def init(self, data):
        self.name = data['name']
        self.description = data['description']
        self.attributes = json.dumps(data['attributes'])
        self.universe_id = data['universe']