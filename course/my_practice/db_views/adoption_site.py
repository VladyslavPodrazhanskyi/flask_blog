import os
from flask import Flask, render_template, url_for, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from forms import AddForm, DelForm, AddOwner

app = Flask(__name__)

app.config['SECRET_KEY'] = 'very_secret_key'

#########################################
######### SQL DATABASE SECTION ##########
#########################################
basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'adoption.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

Migrate(app, db)

#####################################
####  MODELS       ###############
#####################################

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

    return render_template('add.html', form=form)


@app.route('/list')
def list_pup():

    puppies = Puppy.query.all()
    return render_template('list.html', puppies=puppies)


@app.route('/delete', methods=['GET', 'POST'])
def del_pup():

    form = DelForm()
    not_id_mess = ''
    if form.validate_on_submit():
        id = form.id.data

        pup_for_del = Puppy.query.get(id)
        if pup_for_del:
            db.session.delete(pup_for_del)
            db.session.commit()
            return redirect(url_for('list_pup'))
        else:
            not_id_mess = f'Sorry, but we do not have the puppy with id: {id} '
            return render_template('delete.html', form=form, not_id_mess=not_id_mess)

    return render_template('delete.html', form=form, not_id_mess=not_id_mess)


@app.route('/add_owner', methods=['GET', 'POST'])
def add_owner():
    form = AddOwner()
    not_id_mess = ''
    if form.validate_on_submit():
        name = form.name.data
        puppy_id = form.puppy_id.data

        cur_pup = Puppy.query.get(puppy_id)

        if cur_pup:
            flash('You successfully added the owner to the puppy!')

            cur_owner = Owner(name, puppy_id)
            cur_pup.owner = cur_owner

            db.session.add_all([cur_owner, cur_pup])
            db.session.commit()

            return redirect(url_for('list_pup'))

        else:
            not_id_mess = f'Sorry, but we do not have the puppy with id: {puppy_id} '
            return render_template('add_owner.html', form=form, not_id_mess=not_id_mess)

    return render_template('add_owner.html', form=form, not_id_mess=not_id_mess)



if __name__ == '__main__':
    app.run(debug=True)


