# users/forms.py

from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed

from wtforms import SubmitField, StringField, PasswordField
from wtforms import ValidationError

from wtforms.validators import DataRequired, EqualTo, Email

from flask_login import current_user
from blog_project.models import User


class LoginForm(FlaskForm):
    email = StringField('Email: ', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')


class RegistrationForm(FlaskForm):
    email = StringField('Email: ', validators=[DataRequired(), Email()])
    username = StringField('Username: ', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), EqualTo('password_confirm', message='Passwords must match')])
    password_confirm = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Register')

    def email_check(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Your email has been registered already!')

    def username_check(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Your username has been registered already!')


class UpdateUserForm(FlaskForm):
    email = StringField('Email: ', validators=[DataRequired(), Email()])
    username = StringField('Username: ', validators=[DataRequired()])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')

    def email_check(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Your email has been registered already!')

    def username_check(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Your username has been registered already!')
