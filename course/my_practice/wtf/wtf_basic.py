from flask import Flask, render_template, url_for, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)

app.config['SECRET_KEY'] = b'MiI\xca\xaf~\x88\xa2\xd9\x07\xd9{\xa5p\xfb\x0b]>(#\x17\xb0\xf7\xf6'


class BreedForm(FlaskForm):
    breed_field = StringField('What breed are you? ')
    submit = SubmitField('Submit')


@app.route('/', methods=['GET', 'POST'])
def index():
    form = BreedForm()
    breed = False
    if form.validate_on_submit():
        breed = form.breed_field.data
        form.breed_field.data = ''
    return render_template('index.html', form=form, breed=breed)


if __name__ == '__main__':
    app.run(debug=True)























# from flask import Flask, render_template
# from flask_wtf import FlaskForm
# from wtforms import StringField, SubmitField
#
#
# app = Flask(__name__)
#
#
# app.config['SECRET_KEY'] = b'\xd6h2\x96J\xe9b\xf4\x92s\xa8\x03\xe2\x92\xb9\xcdh\xfb\xa1Ejq\xc8*'
# # import os
# # os.urandom(24)
#
# class InfoForm(FlaskForm):
#     breed = StringField('What breed are you?')
#     submit = SubmitField('Submit')
#
#
#
# @app.route('/', methods=['GET', 'POST'])
# def index():
#     breed = False
#     form = InfoForm()
#     if form.validate_on_submit():
#         breed = form.breed.data
#         form.breed.data = ""
#     return render_template('index.html', form=form, breed=breed)
#
#
# if __name__ == "__main__":
#     app.run(debug=True)