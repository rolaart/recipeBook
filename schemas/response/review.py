from marshmallow import fields
from marshmallow_enum import EnumField

from models.enums import Review
from schemas.bases import BaseReviewSchema


class ReviewResponseSchema(BaseReviewSchema):
    id = fields.Integer(required=True)
    create_on = fields.DateTime(required=True)
