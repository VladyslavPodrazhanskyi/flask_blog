from flask_wtf import FlaskForm
from wtforms import (StringField, TextAreaField, SelectField,
                     RadioField,TextField,BooleanField,
                     DateTimeField,SubmitField)
from wtforms.validators import DataRequired


class InfoForm(FlaskForm):
    breed = StringField('What breed you are?', validators=[DataRequired()])
    neutered = BooleanField('Have you been neutered?')
    feedback = TextAreaField('Leave your feedback')
    mood = RadioField('Please choose your mood:',
                      choices=[('mood_one', 'happy'), ('mood_two', 'excited')])
    food = SelectField(u'Pick your favorite food',
                       choices=[('fsh', 'fish'), ('bn', 'bones'), ('mt', 'meat')])
    submit = SubmitField('Submit')
