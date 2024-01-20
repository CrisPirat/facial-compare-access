from .models import *


def getUsers():
    result = []
    result = User.query.all()
    return [item.toJson() for item in result]


def setUser(form):
    pass


def getUser(user_id):
    result = User.query.filter_by(id=user_id).first()
    return result.toJson if result else None


def updateUser(form):
    pass
