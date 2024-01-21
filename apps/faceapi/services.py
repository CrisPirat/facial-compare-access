from .models import *
from apps import db


def getUsers():
    result = []
    result = User.query.all()
    return [item for item in result]


def setUser(encoding, url_picture, form):
    try:
        new_user = User(**form)
        new_user.encoding = encoding
        new_user.gender = 'M'
        new_user.status = 'A'
        new_user.url_picture = url_picture
        db.session.add(new_user)
        db.session.commit()
    except Exception as e:
        print('Error {}'.format(e))
        return False
    return True


def getUser(user_id):
    result = User.query.filter_by(id=user_id).first()
    return result if result else None


def updateUser(form):
    pass
