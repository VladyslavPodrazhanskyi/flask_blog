# login/forms.py
from myproject import app, db, login_manager
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, PasswordField, IntegerField
from wtforms.validators import DataRequired, EqualTo, Email
from wtforms import ValidationError
from myproject.models import User

class LoginForm(FlaskForm):
    email = StringField('Email: ', validators=[DataRequired(), Email()])
    password = PasswordField('Password: ', validators=[DataRequired()])
    submit = SubmitField('Login: ')


class RegisterForm(FlaskForm):
    email = StringField('Email: ', validators=[DataRequired(), Email()])
    username = StringField('Username: ', validators=[DataRequired()])
    password = PasswordField('Password: ', validators=[DataRequired(), EqualTo('password_confirm', message='Passwords must match!')])
    password_confirm = PasswordField('Confirm password: ', validators=[DataRequired()])
    submit = SubmitField('Register: ')

    def email_check(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('User with current email is registered already')

    def username_check(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('User with current name is registered already')











