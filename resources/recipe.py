from flask_restful import Resource

from managers.auth import auth
from managers.recipe import RecipeManager
from managers.review import ReviewManager
from models.enums import RoleType
from flask import request

from schemas.request.recipe import RequestRecipeSchema
from schemas.response.recipe import RecipeResponseSchema
from utils.decorators import permission_required, validate_schema


class RecipeListCreate(Resource):
    @auth.login_required
    def get(self):
        user = auth.current_user()
        recipes = RecipeManager.get_all_recipes(user)
        # Use dump, not load when schema and object are not the same
        return RecipeResponseSchema().dump(recipes, many=True)

    @auth.login_required
    @permission_required(RoleType.cook)
    @validate_schema(RequestRecipeSchema)
    def post(self):
        cook = auth.current_user()
        data = request.get_json()
        recipe = RecipeManager.create(data, cook)
        # Use dump, not load when schema and object are not the same
        return RecipeResponseSchema().dump(recipe)


class Recipe(Resource):
    def get(self):
        recipes = RecipeManager.get_all_recipes()
        return RecipeResponseSchema().dump(recipes)


class GoodReview(Resource):
    @auth.login_required
    @permission_required(RoleType.critique)
    def put(self, id_, review):
        ReviewManager.good_review(id_, review)
        return 200


class AverageReview(Resource):
    @auth.login_required
    @permission_required(RoleType.critique)
    def put(self, id_, review):
        ReviewManager.average_review(id_, review)
        return 200


class BadReview(Resource):
    @auth.login_required
    @permission_required(RoleType.critique)
    def put(self, id_, review):
        ReviewManager.bad_review(id_, review)
        return 200


class DeleteRecipe(Resource):
    @auth.login_required
    def delete(self, id_):
        RecipeManager.delete(id_)
        return 204
