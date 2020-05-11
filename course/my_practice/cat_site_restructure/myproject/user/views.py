from flask import (Blueprint, redirect, render_template,
                   url_for, flash, request)
from myproject import db
from myproject.user.forms import LoginForm, RegisterForm
from myproject.models import User
from flask_login import login_user, logout_user, login_required


user_blueprint = Blueprint('user', __name__, template_folder='templates/user')



@user_blueprint.route('/welcome')
@login_required
def welcome():
    return render_template('welcome.html')



@user_blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    flash("You're logged out!")
    return redirect(url_for('index'))


@user_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        print(type(user))
        if user.check_password(form.password.data) and user is not None:
            login_user(user)
            flash("You're logged in successfully!")
            # сохраняем запрос, который пользователь делал будуче незалогиненным.
            next = request.args.get('next')
            if next == None or not next[0] == '/':
                next = url_for('user.welcome')
            return redirect(next)
    return render_template('login.html', form=form)


@user_blueprint.route('/register', methods=["GET", "POST"])
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
        return redirect(url_for('user.login'))
    return render_template('register.html', form=form)



