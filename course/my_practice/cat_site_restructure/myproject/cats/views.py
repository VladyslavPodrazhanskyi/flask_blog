# myproject/cats/views.py

from flask import Blueprint, redirect, render_template, url_for
from myproject import db
from myproject.cats.forms import AddForm, DelForm
from myproject.models import Cat
from flask_login import login_required

cats_blueprint = Blueprint('cats', __name__, template_folder='templates/cats')


@cats_blueprint.route('/list')
def cat_list():
    cats = Cat.query.all()
    return render_template('list.html', cats=cats)



@cats_blueprint.route('/add', methods=['GET', 'POST'])
@login_required
def add_cat():
    form = AddForm()
    if form.validate_on_submit():
        name = form.cat_name.data
        new_cat = Cat(name)
        db.session.add(new_cat)
        db.session.commit()
        return redirect(url_for('cats.cat_list'))
    return(render_template('add.html', form=form))



@cats_blueprint.route('/delete', methods=['POST', 'GET'])
@login_required
def del_cat():
    form = DelForm()
    if form.validate_on_submit():
        cat_id = form.cat_id.data
        cat_to_del = Cat.query.get(cat_id)
        db.session.delete(cat_to_del)
        db.session.commit()
        return redirect(url_for('cats.cat_list'))
    return render_template('delete.html', form=form)
