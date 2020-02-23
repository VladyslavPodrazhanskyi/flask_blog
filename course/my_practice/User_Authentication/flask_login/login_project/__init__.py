# __init__.py


import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
# The login manager contains the code
# that lets your application and Flask-Login work together,
# such as how to load a user from an ID, where to send users
# when they need to log in, and the like.

login_manager = LoginManager()

app = Flask(__name__)

app.config['SECRET_KEY'] = 'very secret'

basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'login.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)

login_manager.init_app(app)

login_manager.login_view = 'login'  # name of view functin where login manager will be used
