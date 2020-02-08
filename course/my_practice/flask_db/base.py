import os  # let grab path and file names
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

########################################
basedir = os.path.abspath(os.path.dirname(__file__))
# __file__ - name of current file (base.py)
# os.path.dirname(__file__) - return dir name of base.py (flask_db)
# os.path.abspath(os.path.dirname(__file__)) -  returns absolute path of directory flask db
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# Create a database

db = SQLAlchemy(app)

#################################
# Create models  - tables of DB:

class Puppy(db.Model):
    __tablename__ = 'puppies'  # Manually override table name Puppy (by default as class name
    #create columns of the table:
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    age = db.Column(db.Integer)

    def __init__(self, name, age):   # id as primary_key is created automatically
        self.name = name
        self.age = age

    def __repr__(self):
        return f'Puppy {self.name}  is {self.age} year/s old.'





if __name__ == "__main__":
    app.run(debug=True)