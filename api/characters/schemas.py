from marshmallow import Schema, fields


class CharacterSchema(Schema):
    """Schema mirrors the model without the searchables"""
    name = fields.Str()
    description = fields.Str()
    universe_id = fields.Integer()
    attributes = fields.Raw()
