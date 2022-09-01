from flask_restful import Resource

from managers.auth import auth
from managers.recipe import RecipeManager
from managers.review import ReviewManager
from models.enums import RoleType
from flask import request

# from schemas.request.complain import RequestComplainSchema
# from schemas.response.complain import ComplaintResponseSchema
# from utils.decorators import permission_required, validate_schema


class RecipeListCreate(Resource):
    @auth.login_required
    def get(self):
        user = auth.current_user()
        recipes = RecipeManager.get_all_recipe(user)
        # Use dump, not load when schema and object are not the same
        # return ComplaintResponseSchema().dump(recipes, many=True)

    @auth.login_required
    # @permission_required(RoleType.cook)
    # @validate_schema(RequestComplainSchema)
    def post(self):
        cook = auth.current_user()
        data = request.get_json()
        recipe = RecipeManager.create(data, cook)
        # Use dump, not load when schema and object are not the same
        # return ComplaintResponseSchema().dump(complain)


class GoodReview(Resource):
    # @auth.login_required
    # @permission_required(RoleType.critique)
    def put(self, id_, review):
        ReviewManager.good_review(id_, review)
        return 200


class AverageReview(Resource):
    # @auth.login_required
    # @permission_required(RoleType.critique)
    def put(self, id_, review):
        ReviewManager.average_review(id_, review)
        return 200


class BadReview(Resource):
    # @auth.login_required
    # @permission_required(RoleType.critique)
    def put(self, id_, review):
        ReviewManager.bad_review(id_, review)
        return 200
