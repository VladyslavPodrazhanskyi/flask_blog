from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import RadioField, SelectField, SubmitField, TextAreaField

app = Flask(__name__)

app.config['SECRET_KEY'] = b'f3:\x18\x0e\x97\x17\xc9\xee5\xdcI\xd7\xd3\xec\x83u3\x94\xc24\x0b\x82\xf8'
# >>> import os
# >>> os.urandom(24)

class PupAdoptForm(FlaskForm):
    own = RadioField(choices=[('yes', 'yes'), ('no', 'no')])
    clean = SelectField(choices=[('Great', '3'), ('OK', '2') , ('Bad', '1')])
    comments = TextAreaField()
    submit = SubmitField('Submit Feedback')


#
#
#
# @app.route('/', methods=['GET', 'POST'])
# def index():
#     form = InfoForm()
#     if form.validate_on_submit():
# # session is necessary to save data from filled form
# # and pass information to redirect
# # Session is not appropriate for permanent saving information
# # (get post redirect get)
#         session['breed'] = form.breed.data
#         session['neutered'] = form.neutered.data
#         session['mood'] = form.mood.data
#         session['food'] = form.food.data
#         session['feedback'] = form.feedback.data
#         # action for form
#         return redirect(url_for('thankyou'))
#     return render_template('index.html', form=form)


@app.route('/')
def index():
    return '<h1>Welcome to form training site!</h1>'

@app.route('/puppy_adoption_form')
def paf():
    form = PupAdoptForm()
    return render_template('puppy_adoption_form.html', form=form)





if __name__ == "__main__":
    app.run(debug=True)