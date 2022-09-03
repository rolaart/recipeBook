from flask_restful import Resource
from flask import request

from managers.auth import auth
from managers.recipe import RecipeManager
from managers.review import ReviewManager
from managers.user import UserManager
from models.enums import RoleType
from schemas.request.user import RequestCreateCritiqueSchema, RequestCreateAdimSchema
from utils.decorators import validate_schema, permission_required


class CreateAdmin(Resource):
    @auth.login_required
    @permission_required(RoleType.admin)
    @validate_schema(RequestCreateAdimSchema)
    def post(self):
        data = request.get_json()
        UserManager.create_admin(data)
        return 201


class CreateCritique(Resource):
    @auth.login_required
    @permission_required(RoleType.admin)
    @validate_schema(RequestCreateCritiqueSchema)
    def post(self):
        data = request.get_json()
        # Here we add logic to store the certificate's photo in S3
        UserManager.create_critique(data)
        return 201


class RecipeManagement(Resource):
    @auth.login_required
    @permission_required(RoleType.admin)
    def delete(self, id_):
        RecipeManager.delete(id_)
        return 204


class ReviewManagement(Resource):
    @auth.login_required
    @permission_required(RoleType.admin)
    def delete(self, id_):
        ReviewManager.delete(id_)
        return 204
