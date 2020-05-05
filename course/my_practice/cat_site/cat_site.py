import os
from flask import Flask, render_template, url_for, redirect, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from forms import AddForm, DelForm, AddOwnerForm


app = Flask(__name__)

app.config['SECRET_KEY'] = b'mh\xd6l\x0bV\xde\xf2\xa5\x96X6Ck\xdco\x07E\x8c\x8d\xfco\xbcQ'

##### DB section ######

base_dir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(base_dir, 'cat_site.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)


###### MODELS #####

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


##### Views ######
@app.route('/')
def index():
    return render_template('home.html')


@app.route('/list')
def list():
    cats = Cat.query.all()
    return render_template('list.html', cats=cats)


@app.route('/add_cat', methods=['GET', 'POST'])
def add_cat():
    form = AddForm()
    if form.validate_on_submit():
        name = form.cat_name.data
        new_cat = Cat(name)
        db.session.add(new_cat)
        db.session.commit()
        return redirect(url_for('list'))
    return(render_template('add.html', form=form))


@app.route('/del', methods=['POST', 'GET'])
def del_cat():
    form = DelForm()
    if form.validate_on_submit():
        cat_id = form.cat_id.data
        cat_to_del = Cat.query.get(cat_id)
        db.session.delete(cat_to_del)
        db.session.commit()
        return redirect(url_for('list'))
    return render_template('delete.html', form=form)

@app.route('/add_owner', methods=['POST', 'GET'])
def add_owner():
    form = AddOwnerForm()
    if form.validate_on_submit():
        owner_name = form.owner.data
        cat_id = form.cat_id.data
        cur_owner = Owner(owner_name, cat_id)
        db.session.add(cur_owner)
        db.session.commit()
        return redirect(url_for('list'))
    return render_template('add_owner.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)