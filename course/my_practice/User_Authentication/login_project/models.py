# models.py

from login_project import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin  # встроенный класс от которого будем наследоваться
# и использовать его встроенные атрибуты

# create user loader ( функция, кот загружает пользователя принимая его id в качестве аргумента)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)



class User(db.Model, UserMixin):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))

    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password_hash = generate_password_hash(password)


    def check_password(self, password):
        return check_password_hash(self.password_hash, password)





