from db import db


class ReviewModel(db.Model):
    __tablename__ = 'reviews'

    id = db.Column(db.Integer, primary_key=True)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipes.id'))
    recipe = db.relationship('RecipeModel')
    critique_id = db.Column(db.Integer, db.ForeignKey('critiques.id'))
    critique = db.relationship('CritiqueModel')
