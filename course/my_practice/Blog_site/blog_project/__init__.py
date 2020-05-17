# blog_project/__init__.py
import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)

app.config['SECRET_KEY'] = b'\xa4J\x86/\xd9\xe3Y\x05\xdbs\x92w\xe0t\xea\xc3\xda\xa4\x94w\x1f\x9a\xfb\xa1'

########################################################
#########    DATABASE SETUP    #########################
########################################################

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'blog.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)
Migrate(app, db)


#####################################################
# LOGIN CONFIGS

login_manager = LoginManager()

login_manager.init_app(app)
login_manager.login_view = 'users.login'



from blog_project.core.views import core
from blog_project.users.views import users
from blog_project.blog_posts.views import blog_posts

from blog_project.error_pages.handlers import error_pages


app.register_blueprint(core)
app.register_blueprint(users)
app.register_blueprint(error_pages)
app.register_blueprint(blog_posts)