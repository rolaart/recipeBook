from db import db
from models.review import ReviewModel
from models.user import CritiqueModel, CookModel
from models.recipe import RecipeModel
from models.enums import Review


class ReviewManager:
    @staticmethod
    def get_all_reviews_per_recipe(recipe):
        if isinstance(recipe, RecipeModel):
            return ReviewModel.query.filter_by(recipe_id=recipe.id).all()
        return RecipeModel.query.all()

    @staticmethod
    def get_all_reviews_per_critique(user):
        if isinstance(user, CritiqueModel):
            return ReviewModel.query.filter_by(critique_id=user.id).all()
        return RecipeModel.query.all()

    @staticmethod
    def create(data, critique):
        """
        Decode the base64 encoded photo,
        uploads it to s3 and set the photo url to
        the s3 generated url.
        Creates a complaint and issues a transaction against it.
        Flushes the rows.
        """
        data["critique_id"] = critique.id
        r = Review(**data)
        db.session.add(r)
        db.session.flush()
        return r

    @staticmethod
    def delete(id_):
        ReviewModel.query.filter_by(id=id_).delete()

    @staticmethod
    def bad_review(id_, review):
        ReviewModel.query.filter_by(id=id_).update({"review": Review.bad})
        ReviewModel.query.filter_by(id=id_).update({"description": review})

    @staticmethod
    def average_review(id_, review):
        ReviewModel.query.filter_by(id=id_).update({"description": review})

    @staticmethod
    def good_review(id_, review):
        ReviewModel.query.filter_by(id=id_).update({"review": Review.good})
        ReviewModel.query.filter_by(id=id_).update({"description": review})
