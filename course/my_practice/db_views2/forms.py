from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField

class AddForm(FlaskForm):
    cat_name = StringField('Name of the Cat: ')
    submit = SubmitField('Add cat')

class DelForm(FlaskForm):
    cat_id = IntegerField('Id of the Cat to remove: ')
    submit = SubmitField('Remove the cat')

class AddOwnerForm(FlaskForm):
    owner = StringField('Name of Owner: ')
    cat_id = IntegerField('Id of Cat: ')
    submit = SubmitField('Add Owner')