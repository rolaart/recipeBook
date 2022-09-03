from flask_cors import cross_origin
from flask_restful import Resource
from flask import request
from managers.user import CookManager, CritiqueManager, AdminManager
from schemas.request.user import RequestLoginUserSchema, RequestRegisterCookSchema
from utils.decorators import validate_schema


class RegisterCook(Resource):
    @validate_schema(RequestRegisterCookSchema)
    def post(self):
        data = request.get_json()
        token = CookManager.register(data)
        return {"token": token}, 201


class LoginCook(Resource):
    @validate_schema(RequestLoginUserSchema)
    @cross_origin()
    def post(self):
        data = request.get_json()
        token = CookManager.login(data)
        return {"token": token, "role": "cook"}


class LoginCritique(Resource):
    @validate_schema(RequestLoginUserSchema)
    def post(self):
        data = request.get_json()
        token = CritiqueManager.login(data)
        return {"token": token, "role": "critique"}


class LoginAdministrator(Resource):
    @validate_schema(RequestLoginUserSchema)
    def post(self):
        data = request.get_json()
        token = AdminManager.login(data)
        return {"token": token, "role": "admin"}