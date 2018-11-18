from flask import request
from flask_restplus import Resource, Namespace, fields
import json
from characters.schemas import CharacterSchema
from characters.models import Character
from utils import add_record, update_record

api = Namespace('character', description='Character operations')

schema = CharacterSchema()

create_input = api.model('Create: Character', {
    'name': fields.String(required=True),
    'universe_id': fields.Integer(required=True),
    'attributes': fields.String()
})

update_input = api.model('Update: Character', {
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
class CreateCharacter(Resource):
    @staticmethod
    @api.expect(create_input)
    def post():
        data = request.get_json()
        character = add_record(Character(), data)
        return schema.dump(character)


'''
################################################################################
################################################################################
##################################### Read #####################################
################################################################################
################################################################################
'''


@api.route('/all')
class GetAllCharacters(Resource):
    @staticmethod
    def get():
        character = Character.query.all()
        records = []
        for c in character:
            c.attributes = json.loads(c.attributes)
            records.append(schema.dump(c)[0])
        return records


@api.route('/<name>')
@api.doc(params={'name': 'Name of the character to search for'})
class GetCharacterWithoutUniverse(Resource):
    @staticmethod
    def get(name):
        character = Character.query.filter_by(name=name).first()
        character.attributes = json.loads(character.attributes)
        return schema.dump(character)[0]


@api.route('/<universe>/<name>')
@api.doc(params={'name': 'Name of the character to search for', 'universe': 'Universe the character is within'})
class GetCharacterWithUniverse(Resource):
    @staticmethod
    def get(name, universe):
        character = Character.query.filter_by(name=name, universe=universe).first()
        records = []
        for c in character:
            c.attributes = json.loads(c.attributes)
            records.append(schema.dump(c)[0])
        return records


'''
################################################################################
################################################################################
#################################### Update ####################################
################################################################################
################################################################################
'''


@api.route('/update')
class UpdateCharacter(Resource):
    @staticmethod
    @api.expect(update_input)
    def put():
        data = request.get_json()
        character = update_record(Character, data)
        return schema.dump(character)
