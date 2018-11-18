from flask import request
from flask_restplus import Resource, Namespace, fields
import json
from items.schemas import ItemSchema
from items.models import Item
from utils import add_record, update_record

api = Namespace('item', description='Item operations')

schema = ItemSchema()

create_input = api.model('Create: Item', {
    'name': fields.String(required=True),
    'universe': fields.String(required=True),
    'attributes': fields.String()
})

update_input = api.model('Update: Item', {
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
class CreateItem(Resource):
    @staticmethod
    @api.expect(create_input)
    def post():
        data = request.get_json()
        item = add_record(Item(), data)
        return schema.dump(item)


'''
################################################################################
################################################################################
##################################### Read #####################################
################################################################################
################################################################################
'''


@api.route('/all')
class GetAllItems(Resource):
    @staticmethod
    def get():
        item = Item.query.all()
        records = []
        for i in item:
            i.attributes = json.loads(i.attributes)
            records.append(schema.dump(i)[0])
        return records


@api.route('/<name>')
@api.doc(params={'name': 'Name of the item to search for'})
class GetItemWithoutUniverse(Resource):
    @staticmethod
    def get(name):
        item = Item.query.filter_by(name=name).first()
        records = []
        for i in item:
            i.attributes = json.loads(i.attributes)
            records.append(schema.dump(i)[0])
        return records


@api.route('/<universe>/<name>')
@api.doc(params={'name': 'Name of the item to search for', 'universe': 'Universe the item is within'})
class GetItemWithUniverse(Resource):
    @staticmethod
    def get(name, universe):
        item = Item.query.filter_by(name=name, universe=universe).first()
        records = []
        for i in item:
            i.attributes = json.loads(i.attributes)
            records.append(schema.dump(i)[0])
        return records


'''
################################################################################
################################################################################
#################################### Update ####################################
################################################################################
################################################################################
'''


@api.route('/update')
class UpdateItem(Resource):
    @staticmethod
    @api.expect(update_input)
    def put():
        data = request.get_json()
        item = update_record(Item, data)
        return schema.dump(item)
