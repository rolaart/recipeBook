from marshmallow import fields
from schemas.bases import BaseRecipeSchema


class RequestRecipeSchema(BaseRecipeSchema):
    steps = fields.String(required=True)
    photo = fields.String()
