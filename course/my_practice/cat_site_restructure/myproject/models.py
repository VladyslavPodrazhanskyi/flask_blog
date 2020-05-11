# to set up db in __init__.py inside myproject folder
from myproject import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash



class Cat(db.Model):
    __tablename__ = 'cats'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    owner = db.relationship('Owner', backref='Cat', uselist=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        if self.owner:
            return f'Cat name is {self.name}, id is {self.id}, and owner is {self.owner}'
        return f'Cat name is {self.name}, id is {self.id}. It has no owner yet.'


class Owner(db.Model):
    __tablename__ = 'owners'
    owner_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    cat_id = db.Column(db.Integer, db.ForeignKey('cats.id'))

    def __init__(self, name, cat_id):
        self.name = name
        self.cat_id = cat_id

    def __repr__(self):
        return f'Owner name is {self.name}'


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))

    def __init__(self, email, username, password):
        self.name = username
        self.email = email
        self.username = username
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)