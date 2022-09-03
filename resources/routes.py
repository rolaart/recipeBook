from resources.admin import CreateAdmin, CreateCritique, ReviewManagement, \
    RecipeManagement
from resources.auth import RegisterCook, LoginCook, LoginCritique, LoginAdministrator
from resources.recipe import GoodReview, AverageReview, BadReview, RecipeListCreate

routes = (
    (RegisterCook, "/register"),
    (LoginCook, "/login"),
    (RecipeListCreate, "/<int:id_>/list/recipe"),
    (LoginCritique, "/critique/login"),
    (GoodReview, "/critique/review/<int:id_>/good_review"),
    (AverageReview, "/critique/review/<int:id_>/average_review"),
    (BadReview, "/critique/review/<int:id_>/bad_review"),
    (RecipeListCreate, "/cooks/recipes"),
    (CreateAdmin, "/admins/create-admin"),
    (CreateCritique, "/admins/create-critique"),
    (ReviewManagement, "/admins/reviews/<int:id_>"),
    (RecipeManagement, "/admins/recipes/<int:id_>"),
    (LoginAdministrator, "/admins/login"),
)
