from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)

app.config["SECRET_KEY"] = 'very_secret_key'

class Infoform(FlaskForm):
    breed_field = StringField("What breed are you?")
    submit = SubmitField('Submit')

@app.route('/', methods=['POST', 'GET'])
def index():
    form = Infoform()
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
# app.config['SECRET_KEY'] = 'mysecretkey'
#
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