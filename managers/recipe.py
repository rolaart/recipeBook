import os
import uuid

from constraints import TEMP_FILE_FOLDER
from db import db
from models.user import CookModel
from models.recipe import RecipeModel
from utils.helpers import decode_photo


class RecipeManager:
    @staticmethod
    def get_all_recipes(user):
        if isinstance(user, CookModel):
            return RecipeModel.query.filter_by(cook_id=user.id).all()
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
        encoded_photo = data.pop("photo")
        extension = data.pop("photo_extension")
        name = f"{str(uuid.uuid4())}"
        path = os.path.join(TEMP_FILE_FOLDER, f"{name}.{extension}")
        decode_photo(path, encoded_photo)
        # url = s3.upload_photo(path, name, extension)
        # data["photo"] = url
        r = RecipeModel(**data)
        db.session.add(r)
        db.session.flush()
        return r

    @staticmethod
    def delete(id_):
        RecipeManager.query.filter_by(id=id_).delete()
