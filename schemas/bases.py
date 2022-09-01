from marshmallow import Schema, fields


class BaseRecipeSchema(Schema):
    title = fields.String(required=True)
    description = fields.String(required=True)


class BaseReviewSchema(Schema):
    description = fields.String(required=True)
