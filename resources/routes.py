from resources.admin import CreateAdmin, CreateCritique, ReviewManagement, \
    RecipeManagement
from resources.auth import RegisterCook, LoginCook, LoginCritique, LoginAdministrator
from resources.recipe import GoodReview, AverageReview, BadReview, RecipeListCreate, Recipe, DeleteRecipe

routes = (
    # post
    (RegisterCook, "/register"),
    (LoginCook, "/login"),
    (LoginCritique, "/critique/login"),
    (CreateAdmin, "/admins/create-admin"),
    (CreateCritique, "/admins/create-critique"),
    (LoginAdministrator, "/admins/login"),
    # get
    (Recipe, "/recipe"),
    (RecipeListCreate, "/cooks/recipes"),
    # put
    (GoodReview, "/critique/review/<int:id_>/good_review"),
    (AverageReview, "/critique/review/<int:id_>/average_review"),
    (BadReview, "/critique/review/<int:id_>/bad_review"),
    # delete
    (ReviewManagement, "/admins/reviews/<int:id_>"),
    (RecipeManagement, "/admins/recipes/<int:id_>"),
    (DeleteRecipe, "/recipe/<int:id_>/delete"),
)
