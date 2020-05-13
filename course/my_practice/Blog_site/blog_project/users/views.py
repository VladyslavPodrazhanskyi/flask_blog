# users/views.py

# login
# logout
# register
# account
# list of users blog

from flask import (Blueprint, render_template, redirect,
                   flash, url_for, request)
from blog_project import db
from blog_project.models import User, BlogPost
from blog_project.users.forms import RegistrationForm, LoginForm, UpdateUserForm
from flask_login import login_required, login_user, logout_user, current_user


users = Blueprint('users', __name__)



# login
# logout
# register
# account
# list of users blog