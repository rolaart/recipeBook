from db import db
from models.enums import RoleType


class BaseUserModel(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    phone = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(255), nullable=False)


class CookModel(BaseUserModel):
    __tablename__ = 'cooks'

    cooks = db.relationship("RecipeModel", db.backref("cook"))
    role = db.Column(
        db.Enum(RoleType),
        default=RoleType.cook,
        nullable=False
    )


class CritiqueModel(BaseUserModel):
    __tablename__ = 'critiques'

    certificate = db.Column(db.String(255), nullable=False)
    critiques = db.relationship("ReviewModel", db.backref("critique"))
    role = db.Column(
        db.Enum(RoleType),
        default=RoleType.critique,
        nullable=False
    )


class AdministratorModel(BaseUserModel):
    __tablename__ = 'administrators'

    role = db.Column(
        db.Enum(RoleType),
        default=RoleType.admin,
        nullable=False
    )
