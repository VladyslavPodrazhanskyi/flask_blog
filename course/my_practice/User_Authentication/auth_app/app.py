from app_project import app, db
from flask import (render_template, url_for,
                   redirect, request, abort, flash)
from flask_login import login_required, login_user, logout_user
from app_project.models import User
from app_project.forms import RegisterForm, LoginForm



@app.route('/')
def index():
    return render_template('home.html')


@login_required
@app.route('/welcome')
def welcome():
    return render_template('welcome.html')


@login_required
@app.route('/logout')
def logout():
    logout_user()
    flash("You're logged out!")
    return redirect(url_for('index'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user.check_pass(form.password.data) and user is not None:
            login_user(user)
            flash("You're logged in successfully!")
            # сохраняем запрос, который пользователь делал будуче незалогиненным.
            next = request.args.get('next')
            if next == None or not next[0] == '/':
                next = url_for('welcome')
            return redirect(next)
    return render_template('login.html', form=form)


@app.route('/register', methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        # form.check_email()
        # form.check_username()
        new_user = User(form.email.data,
                        form.username.data,
                        form.password.data)
        db.session.add(new_user)
        db.session.commit()
        flash('Thanks for registration')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)


if __name__ == "__main__":
    app.run(debug=True)