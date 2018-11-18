from flask import request
from flask_restplus import Resource, Namespace, fields
import json

from universe.schemas import UniverseSchema
from universe.models import Universe
from utils import add_record, update_record

api = Namespace('universe', description='Universe operations')


schema = UniverseSchema()

create_input = api.model('Create: Universe', {
    'name': fields.String(required=True),
    'description': fields.String,
    'attributes': fields.String
})

update_input = api.model('Update: Universe', {
    'id': fields.Integer(required=True),
    'name': fields.String(required=True),
    'description': fields.String,
    'attributes': fields.String
})
'''
################################################################################
################################################################################
#################################### Create ####################################
################################################################################
################################################################################
'''


@api.route('/create')
class CreateUniverse(Resource):
    @staticmethod
    @api.expect(create_input)
    def post():
        data = request.get_json()
        universe = add_record(Universe(), data)
        return schema.dump(universe)


'''
################################################################################
################################################################################
##################################### Read #####################################
################################################################################
################################################################################
'''


@api.route('/<name>')
class GetUniverseByName(Resource):
    @staticmethod
    def get(name):
        universe = Universe.query.filter_by(name=name).first()
        records = []
        for u in universe:
            u.attributes = json.loads(u.attributes)
            records.append(schema.dump(u)[0])
        return records


@api.route('/all')
class GetAllUniverses(Resource):
    @staticmethod
    def get():
        universe = Universe.query.all()
        records = []
        for u in universe:
            u.attributes = json.loads(u.attributes)
            records.append(schema.dump(u)[0])
        return records


'''
################################################################################
################################################################################
#################################### Update ####################################
################################################################################
################################################################################
'''


@api.route('/update')
class UpdateUniverse(Resource):
    @staticmethod
    @api.expect(update_input)
    def put():
        data = request.get_json()
        universe = update_record(Universe, data)
        return schema.dump(universe)
