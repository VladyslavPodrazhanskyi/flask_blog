# myproject/owners/views.py

from flask import (Blueprint, render_template,
    redirect, url_for, flash)

from myproject import db   # import from __init_.py under myproject folder
from myproject.models import Owner, Puppy
from myproject.owners.forms import AddForm


owners_blueprint = Blueprint('owners', __name__,
                             template_folder='templates/owners')

# @app.route('/add_owner', methods=['GET', 'POST'])
@owners_blueprint.route('/add', methods=['GET', 'POST'])
def add():

    form = AddForm()

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

            return redirect(url_for('puppies.list'))

        else:
            not_id_mess = f'Sorry, but we do not have the puppy with id: {puppy_id} '
            return render_template('add_owner.html', form=form, not_id_mess=not_id_mess)

    return render_template('add_owner.html', form=form, not_id_mess=not_id_mess)
