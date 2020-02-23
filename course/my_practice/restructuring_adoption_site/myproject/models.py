# Models.py
# Set up db inside the __init__.py under myproject forlder

from myproject import db

class Puppy(db.Model):

    __tablename__ = 'puppies'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    owner = db.relationship('Owner', backref='Puppy', uselist=False )

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        if self.owner:
            return f'Puppy name is {self.name} , id is {self.id} and owner is {self.owner.name}'
        return f'Puppy name is {self.name} id is {self.id} and has no owner assigned yet'

class Owner(db.Model):

    __tablename__ = 'owners'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    puppy_id = db.Column(db.Integer, db.ForeignKey('puppies.id'))

    def __init__(self, name, puppy_id):
        self.name = name
        self.puppy_id = puppy_id

    def __repr__(self):
        return f'Owner name: {self.name}'
