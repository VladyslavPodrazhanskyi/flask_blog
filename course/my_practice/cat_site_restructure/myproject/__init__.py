import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SECRET_KEY'] = b'\x9aS\xe6\x8a\x9f\x88\x98\xe42\x9f\x92\xfa\xb4\x83M3\x91\xae\x0b\xb9U\xfc\x96x'

##### DB section ######

base_dir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(base_dir, 'cat_site_restr.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db: SQLAlchemy = SQLAlchemy(app)
Migrate(app, db)


from myproject.cats.views import cats_blueprint
from myproject.owners.views import owners_blueprint

app.register_blueprint(owners_blueprint, url_prefix='/owners')
app.register_blueprint(cats_blueprint, url_prefix='/cats')


