# blog_posts/views.py


from flask import Blueprint


blog_posts = Blueprint('blog_post', __name__)

@blog_posts.route("/<int:blog_post_id")
def blog_post(blog_post_id)