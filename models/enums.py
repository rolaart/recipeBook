import enum


class RoleType(enum.Enum):
    cook = "cook"
    critique = "critique"
    admin = "admin"


class Review(enum.Enum):
    bad = "bad"
    average = "average"
    good = "good"
