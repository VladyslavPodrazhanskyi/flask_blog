import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'relation.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)

######## Models ######

class Puppy(db.Model):
    __tablename__ = 'puppies'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    toys = db.relationship
    owner = None

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        if self.owner:
            return f'The puppy has name {self.name}, owner is {self.owner.name}'
        return f'The puppy has name {self.name}'

    def report_toys(self):
        if self.toys:
            print('Here are my toys:')
            for toy in self.toys:
                print(toy)
        else:
            print('The puppy has no toys yet')

    class Toy(db.Model):
        __tablename__ = 'toys'
        id = db.Column(db.Integer, primary_key=True)
        item_name = db.Column(db.Text)
        puppy_id = db.ForeignKey()


########

if __name__ == '__main__':
    app.run(debug=True)

