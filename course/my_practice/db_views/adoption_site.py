import os
from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from forms import AddForm, DelForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'very_secret_key'

#########################################
######### SQL DATABASE SECTION ##########
#########################################
basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'adoption.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

db = SQLAlchemy(app)

Migrate(app, db)

#####################################
####  MODELS       ###############
#####################################

class Puppy(db.Model):

    __tablename__ = 'puppies'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'Puppy name is {self.name}'

################################################
############  VIEW FUNCTIONS - Having FORMS ############
################################################

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/add', methods=['GET', 'POST'])
def add_pup():

    form = AddForm()
    if form.validate_on_submit():
        name = form.name.data

        new_pup = Puppy(name)
        db.session.add(new_pup)
        db.session.commit()

        return redirect(url_for('list_pup'))

    return render template('add.html', form=form)


@app.route('/list')
def list_pup():

    puppies = Puppy.query.all()
    return render_template('list.html', puppies=puppies)


@app.route('/delete', methods=['GET', 'POST'])
def del_pup():

    form = DelForm()
    if form.validate_on_submit():
        id = form.id.data

        pup_for_del = Puppy.query.get(id)
        db.session.delete(pup_for_del)
        db.session.commit()

        return redirect(url_for('list_pup'))
    return render('delete.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)


