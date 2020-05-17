# blog_posts/views.py

from flask import (Blueprint, url_for, request,
                   render_template, flash, redirect, abort)
from flask_login import login_required, current_user
from blog_project import db
from blog_project.blog_posts.forms import BlogPostForm
from blog_project.models import BlogPost


blog_posts = Blueprint('blog_posts', __name__)

# Create

@blog_posts.route('/create_post', methods=['GET', 'POSt'])
@login_required
def create_post():
    form = BlogPostForm()
    if form.validate_on_submit():
        blog_post = BlogPost(title=form.title.data,
                        text = form.text.data,
                        user_id = current_user.id)
        db.session.add(blog_post)
        db.session.commit()
        flash('Blog post created!')
        return redirect(url_for('core.index'))
        # return redirect(url_for('blog_post', blog_post_id=current_user.id))
    return render_template('create_post.html', form=form)


# Blog post

# @blog_posts.route("/blog_post/<int:blog_post_id")
@blog_posts.route("/<int:blog_post_id>")
def blog_post(blog_post_id):
    blog_post = BlogPost.query.get_or_404(blog_post_id) # ??? first()
    return render_template('blog_post.html', post=blog_post)
    # return render_template('blog_post.html', post=blog_post,
    #                        date=blog_post.date, title=blog.post.title)

# Update
# @blog_posts.route('/update_post/<int:blog_post_id', methods=['GET', 'POSt'])
@blog_posts.route('/<int:blog_post_id>/update', methods=['GET', 'POST'])
@login_required
def update(blog_post_id):
    blog_post = BlogPost.query.get_or_404(blog_post_id)
    # if blog_post.user_id == current_user.id:
    if blog_post.author != current_user:
        abort(403)
    form = BlogPostForm()
    if form.validate_on_submit():
        blog_post.title = form.title.data
        blog_post.text = form.text.data
        db.session.commit()
        flash('Blog post updated')
        return redirect(url_for('blog_posts.blog_post', blog_post_id=blog_post_id))
    # rendering filled form
    elif request.method == 'GET':
        form.title.data = blog_post.title
        form.text.data = blog_post.text
    # it is necessary to mention title in create_post.html
    return render_template('create_post.html', form=form, title='Updating')


# Delete( do not create special page_
# just button for deletion of the blog post
@blog_posts.route('/<int:blog_post_id>/delete', methods=['GET', 'POST'])
@login_required
def delete_post(blog_post_id):
    blog_post = BlogPost.query.get_or_404(blog_post_id)
    if blog_post.author != current_user:
        abort(403)
    db.session.delete(blog_post)
    db.session.commit()
    flash('The blog post is deleted')
    return redirect(url_for('core.index'))


