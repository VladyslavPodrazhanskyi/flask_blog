# users/views.py

# login
# logout
# register
# account
# list of users blog

from flask import (Blueprint, render_template, redirect,
                   flash, url_for, request)
from flask_login import login_required, login_user, logout_user, current_user
from blog_project import db
from blog_project.models import User, BlogPost
from blog_project.users.forms import RegistrationForm, LoginForm, UpdateUserForm
from blog_project.users.picture_handler import add_profile_pic


users = Blueprint('users', __name__)

# login
@users.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user.check_password(form.password.data) and user is not None:
            login_user(user)
            flash('login is successful')
            next = request.args.get('next')
            if next is None or next[0] != '/': # or not next[0] == '/':
                next = url_for('core.index')
            return redirect(next)
    return render_template('login.html', form=form)

# logout
@users.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('core.index'))


# register
@users.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        new_user = User(email=form.email.data,
                        username=form.username.data,
                        password=form.password.data)
        db.session.add(new_user)
        db.session.commit()
        flash('Thank you for registration!')
        return redirect(url_for('users.login'))
    return render_template('register.html', form=form)


# account (Update UserForm)
@users.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateUserForm()
    if form.validate_on_submit():
        if form.picture.data:
            username = current_user.username
            pic = add_profile_pic(form.picture.data, username)
            current_user.profile_image = pic
        current_user.email = form.email.data
        current_user.username = form.username.data
        db.session.commit()
        flash('User account is updated!')
        return redirect(url_for('users.account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email

    profile_image = url_for('static', filename='profile_pics/' + current_user.profile_image)
    return render_template('account.html', profile_image=profile_image, form=form)


# list of users blog

@users.route('/<username>')
# @login_required
def user_posts(username):
    page = request.args.get('page', 1, type=int)
    user = User.query.filter_by(username=username).first_or_404()
    blog_posts = BlogPost.query.filter_by(author=user).order_by(BlogPost.date.desc()).paginate(page=page, per_page=5)
    return render_template('user_blog_posts.html', blog_posts=blog_posts, user=user)


