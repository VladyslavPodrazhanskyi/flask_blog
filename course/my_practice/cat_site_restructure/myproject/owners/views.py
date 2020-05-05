# myproject/owners/views.py

from flask import Blueprint, render_template, redirect, url_for
from myproject.owners.forms import AddForm
from myproject import db
from myproject.models import Owner

owners_blueprint = Blueprint('owners', __name__, template_folder='templates/owners')

@owners_blueprint.route('/add', methods=['POST', 'GET'])
def add_owner():
    form = AddForm()
    if form.validate_on_submit():
        owner_name = form.owner.data
        cat_id = form.cat_id.data
        cur_owner = Owner(owner_name, cat_id)
        db.session.add(cur_owner)
        db.session.commit()
        return redirect(url_for('cats.cat_list')) # !!! changed name of end_point
    return render_template('add_owner.html', form=form)
