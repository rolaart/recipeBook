import os
import uuid

from werkzeug.exceptions import BadRequest
from werkzeug.security import check_password_hash, generate_password_hash

from constraints import TEMP_FILE_FOLDER
from managers.auth import AuthManager
from models.user import CookModel, CritiqueModel, AdministratorModel
from db import db
from services.s3 import S3Service
from utils.helpers import decode_photo


class CookManager:
    @staticmethod
    def register(cook_data):
        """
        Hashes the plain password
        :param cook_data: dict
        :return: cook
        """
        cook_data["password"] = generate_password_hash(cook_data['password'], method='SHA256')
        cook = CookModel(**cook_data)
        try:
            db.session.add(cook)
            db.session.flush()
            return AuthManager.encode_token(cook)
        except Exception as ex:
            raise BadRequest(str(ex))

    @staticmethod
    def login(data):
        """
        Checks the email and password (hashes the plain password)
        :param data: dict -> email, password
        :return: token
        """
        try:
            cook = CookModel.query.filter_by(email=data["email"]).first()
            if cook and check_password_hash(cook.password, data["password"]):
                return AuthManager.encode_token(cook)
            raise Exception
        except Exception:
            raise BadRequest("Invalid username or password")


class UserManager:
    @staticmethod
    def create_admin(data):
        """
        Hashes the plain password
        :param cook_data: dict
        :return: cook
        """
        data["password"] = generate_password_hash(data['password'], method='SHA256')
        admin = AdministratorModel(**data)
        try:
            db.session.add(admin)
            db.session.flush()
            return AuthManager.encode_token(admin)
        except Exception as ex:
            raise BadRequest(str(ex))

    @staticmethod
    def create_critique(data):
        """
        Hashes the plain password
        :param cook_data: dict
        :return: critique
        """
        data["password"] = generate_password_hash(data['password'], method='SHA256')
        s3 = S3Service()
        encoded_photo = data["certificate"]
        extension = data.pop("extension")
        name = f"{str(uuid.uuid4())}.{extension}"
        path = os.path.join(TEMP_FILE_FOLDER, f"{name}")
        decode_photo(path, encoded_photo)
        url = s3.upload_photo(path, name, extension)
        data["certificate"] = url
        critique = CritiqueModel(**data)
        try:
            db.session.add(critique)
            db.session.flush()
            return AuthManager.encode_token(critique)
        except Exception as ex:
            raise BadRequest(str(ex))


class CritiqueManager:
    @staticmethod
    def login(data):
        """
        Checks the email and password (hashes the plain password)
        :param data: dict -> email, password
        :return: token
        """
        try:
            critique = CritiqueManager.query.filter_by(email=data["email"]).first()
            if critique and check_password_hash(critique.password, data["password"]):
                return AuthManager.encode_token(critique)
            raise Exception
        except Exception:
            raise BadRequest("Invalid username or password")


class AdminManager:
    @staticmethod
    def login(data):
        """
        Checks the email and password (hashes the plain password)
        :param data: dict -> email, password
        :return: token
        """
        try:
            admin = AdministratorModel.query.filter_by(email=data["email"]).first()
            if admin and check_password_hash(admin.password, data["password"]):
                return AuthManager.encode_token(admin)
            raise Exception
        except Exception:
            raise BadRequest("Invalid username or password")