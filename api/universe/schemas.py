from marshmallow import Schema, fields


class UniverseSchema(Schema):
    """Schema mirrors the model without the searchables"""
    id = fields.Integer()
    name = fields.Str()
    description = fields.Str()
    attributes = fields.Raw()
