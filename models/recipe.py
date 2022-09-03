from db import db
from sqlalchemy import func


class RecipeModel(db.Model):
    __tablename__ = 'recipes'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    photo_url = db.Column(db.String(255))
    create_on = db.Column(db.DateTime, server_default=func.now())
    ingredients = db.Column(db.String(255))
    steps = db.Column(db.String(255))
    cook_id = db.Column(db.Integer, db.ForeignKey('cooks.id'))
    cook = db.relationship('CookModel')
    reviews = db.relationship('ReviewModel')
