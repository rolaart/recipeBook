from marshmallow import fields
from schemas.bases import BaseRecipeSchema


class RecipeResponseSchema(BaseRecipeSchema):
    id = fields.Integer(required=True)
    ingredients = fields.String()
    steps = fields.String()
    create_on = fields.DateTime(required=True)
    photo_url = fields.URL(required=True)
