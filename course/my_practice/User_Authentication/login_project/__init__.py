# __init__.py

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


app = Flask(__name__)

app.config['SECRET_KEY'] = b'2\xdc\xe9\x84\xfb-\n%E6;\xf4\x9eL;"u[\xd9\xa8\x9b\xb7\xa1&'

basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'login2.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)
Migrate(app, db)


login_manager = LoginManager()
login_manager.init_app(app)      # инициируем наше приложение к созданному менеджеру логинов
login_manager.login_view = 'login'   # указываем вьюху в кот. будет действовать менеджер.