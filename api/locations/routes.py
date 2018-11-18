from flask import request
from flask_restplus import Resource, Namespace, fields
import json
from locations.schemas import LocationSchema
from locations.models import Location
from utils import add_record, update_record

api = Namespace('location', description='Locations operations')


schema = LocationSchema()

create_input = api.model('Create: Location', {
    'name': fields.String(required=True),
    'universe_id': fields.String(required=True),
    'type': fields.String(required=True),
    'attributes': fields.String()
})

update_input = api.model('Update: Location', {
    'id': fields.Integer(required=True),
    'name': fields.String(required=True),
    'universe': fields.String(required=True),
    'attributes': fields.String()
})
'''
################################################################################
################################################################################
#################################### Create ####################################
################################################################################
################################################################################
'''


@api.route('/create')
class CreateLocation(Resource):
    @staticmethod
    @api.expect(create_input)
    def post():
        data = request.get_json()
        location = add_record(Location(), data)
        return schema.dump(location)


'''
################################################################################
################################################################################
##################################### Read #####################################
################################################################################
################################################################################
'''


@api.route('/all')
class GetAllLocations(Resource):
    @staticmethod
    def get():
        location = Location.query.all()
        records = []
        for l in location:
            l.attributes = json.loads(l.attributes)
            records.append(schema.dump(l)[0])
        return records



@api.route('/<name>')
class GetLocationByName(Resource):
    @staticmethod
    def get(name):
        location = Location.query.filter_by(name=name).first()
        records = []
        for l in location:
            l.attributes = json.loads(l.attributes)
            records.append(schema.dump(l)[0])
        return records


'''
################################################################################
################################################################################
#################################### Update ####################################
################################################################################
################################################################################
'''


@api.route('/update')
class UpdateLocation(Resource):
    @staticmethod
    @api.expect(update_input)
    def put():
        data = request.get_json()
        location = update_record(Location, data)
        return schema.dump(location)