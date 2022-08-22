from db import db
from sqlalchemy import func

from models.enums import Review


class ReviewModel(db.Model):
    __tablename__ = 'reviews'

    id = db.Column(db.Integer, primary_key=True)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipes.id'))
    recipe = db.relationship('RecipeModel')
    critique_id = db.Column(db.Integer, db.ForeignKey('critiques.id'))
    critique = db.relationship('CritiqueModel')
    create_on = db.Column(db.DateTime, server_default=func.now())
    review = db.Column(
        db.Enum(Review),
        default=Review.average,
        nullable=False
    )
    description = db.Column(db.String(255))

