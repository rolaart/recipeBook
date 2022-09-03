from flask_restful import Resource

from managers.auth import auth
from managers.recipe import RecipeManager
from managers.review import ReviewManager
from models.enums import RoleType
from flask import request


from schemas.request.review import RequestReviewSchema
from schemas.response.review import ReviewResponseSchema
from utils.decorators import permission_required, validate_schema


class ReviewListByReviewCreate(Resource):
    @auth.login_required
    def get(self):
        user = auth.current_user()
        recipes = RecipeManager.get_all_recipes(user)
        reviews = []
        for recipe in recipes:
            reviews.append(ReviewManager.get_all_reviews_per_recipe(recipe))
        # Use dump, not load when schema and object are not the same
        return ReviewResponseSchema().dump(reviews, many=True)

    @auth.login_required
    @permission_required(RoleType.critique)
    @validate_schema(RequestReviewSchema)
    def post(self):
        critique = auth.current_user()
        data = request.get_json()
        review = ReviewManager.create(data, critique)
        # Use dump, not load when schema and object are not the same
        return ReviewResponseSchema().dump(review)
