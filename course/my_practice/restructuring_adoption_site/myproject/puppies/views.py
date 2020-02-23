# puppies --> views.py

from flask import (Blueprint, redirect, render_template,
                   url_for, flash)
from myproject import db
from myproject.models import Puppy, Owner
from myproject.puppies.forms import AddForm, DelForm

puppies_blueprint = Blueprint('puppies', __name__,
                              template_folder='templates/puppies')

@puppies_blueprint.route('/add', methods=['GET', 'POST'])
def add():

    form = AddForm()
    if form.validate_on_submit():
        name = form.name.data

        new_pup = Puppy(name)
        db.session.add(new_pup)
        db.session.commit()

        return redirect(url_for('puppies.list'))

    return render_template('add.html', form=form)


@puppies_blueprint.route('/list')
def list():

    puppies = Puppy.query.all()
    return render_template('list.html', puppies=puppies)


@puppies_blueprint.route('/delete', methods=['GET', 'POST'])
def delete():

    form = DelForm()
    not_id_mess = ''
    if form.validate_on_submit():
        id = form.id.data

        pup_for_del = Puppy.query.get(id)
        if pup_for_del:
            db.session.delete(pup_for_del)
            db.session.commit()
            return redirect(url_for('puppies.list'))
        else:
            not_id_mess = f'Sorry, but we do not have the puppy with id: {id} '
            return render_template('delete.html', form=form, not_id_mess=not_id_mess)

    return render_template('delete.html', form=form, not_id_mess=not_id_mess)
