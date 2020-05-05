# to set up db in __init__.py inside myproject folder
from myproject import db


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