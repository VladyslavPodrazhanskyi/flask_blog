from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField


class AddForm(FlaskForm):
    owner = StringField('Name of Owner: ')
    cat_id = IntegerField('Id of Cat: ')
    submit = SubmitField('Add Owner')