import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'rel.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

Migrate(app, db)

class Puppy(db.Model):

    __tablename__ = 'puppies'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    # One to Many
    # 1 puppy can have many toys
    toys = db.relationship('Toy', backref='Puppy', lazy='dynamic') # backref is not sensitive to register
    # One to One
    owner = db.relationship('Owner', backref='Puppy', uselist=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        if self.owner:
            return f'Puppy {self.name} has owner {self.owner.name} '
        return f'Puppy {self.name} has no owner yet.'

    def report_toys(self):
        if self.toys.all():   # self.toys is sql request, not an empty list
            print('Here are my toys:')
            for toy in self.toys:
                print(toy.item_name)
        else:
            print('I have no toys yet')

class Toy(db.Model):

    __tablename__ = 'toys'

    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.Text)
    puppy_id = db.Column(db.Integer, db.ForeignKey('puppies.id'))

    def __init__(self, item_name, puppy_id):
        self.item_name = item_name
        self.puppy_id = puppy_id


class Owner(db.Model):

    __tablename__ = "owners"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    puppy_id = db.Column(db.Integer, db.ForeignKey('puppies.id'))


    def __init__(self, name, puppy_id):

        self.name = name
        self.puppy_id = puppy_id

    def __repr__(self):
        return f'Owner {self.name}'

if __name__ == '__main__':
    app.run(debug=True)