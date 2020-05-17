from blog_project.models import BlogPost
from flask import Blueprint, request, render_template

core = Blueprint('core', __name__)

@core.route('/')
def index():
    page = request.args.get('page', 1, type=int)
    blog_posts = BlogPost.query.order_by(BlogPost.date.desc()).paginate(page=page, per_page=5)
    return render_template('index.html', blog_posts=blog_posts)

@core.route('/info')
def info():
    return render_template('info.html')

