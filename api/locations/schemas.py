from marshmallow import Schema, fields


class LocationSchema(Schema):
    """Schema mirrors the model without the searchables"""
    name = fields.Str()
    type = fields.Str()
    description = fields.Str()
    universe = fields.Str()
    attributes = fields.Raw()
