from flask import Flask, render_template, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import (StringField, TextAreaField, SelectField,
                     RadioField,TextField,BooleanField,
                     DateTimeField,SubmitField)
from wtforms.validators import DataRequired

app = Flask(__name__)

app.config['SECRET_KEY'] = 'akfjsafjoi'





class InfoForm(FlaskForm):
    breed = StringField('What breed you are?', validators=[DataRequired()])
    neutered = BooleanField('Have you been neutered?')
    feedback = TextAreaField('Leave your feedback')
    mood = RadioField('Please choose your mood:',
                      choices=[('happy','happy' ), ('excited', 'excited')])
    food = SelectField(u'Pick your favorite food',
                       choices=[('fish', 'fish'), ('bones', 'bones'), ('meat', 'meat')])
    submit = SubmitField('Submit')



@app.route('/', methods=['GET', 'POST'])
def index():
    form = InfoForm()
    if form.validate_on_submit():
# session is necessary to save data from filled form
# and pass information to redirect
# Session is not appropriate for permanent saving information
# (get post redirect get)
        session['breed'] = form.breed.data
        session['neutered'] = form.neutered.data
        session['mood'] = form.mood.data
        session['food'] = form.food.data
        session['feedback'] = form.feedback.data
        # action for form
        return redirect(url_for('thankyou'))
    return render_template('index.html', form=form)

@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')


if __name__ == '__main__':
    app.run(debug=True)