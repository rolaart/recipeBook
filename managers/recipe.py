from db import db
from models.user import CookModel
from models.recipe import RecipeModel


class RecipeManager:
    @staticmethod
    def get_all_recipes(user):
        if isinstance(user, CookModel):
            return CookModel.query.filter_by(cook_id=user.id).all()
        return RecipeModel.query.all()

    @staticmethod
    def create(data, cook):
        """
        Decode the base64 encoded photo,
        uploads it to s3 and set the photo url to
        the s3 generated url.
        Creates a complaint and issues a transaction against it.
        Flushes the rows.
        """
        data["cook_id"] = cook.id
        r = RecipeModel(**data)
        db.session.add(r)
        db.session.flush()
        return r

    @staticmethod
    def delete(id_):
        RecipeManager.query.filter_by(id=id_).delete()
