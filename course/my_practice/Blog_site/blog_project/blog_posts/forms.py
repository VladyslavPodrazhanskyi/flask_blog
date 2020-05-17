# blog_posts/forms.py
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, TextAreaField
from wtforms.validators import DataRequired


class BlogPostForm(FlaskForm):
    # __tablename__ = 'blog_posts'
    title = StringField('Title: ', validators=[DataRequired()])
    text = TextAreaField('Text', validators=[DataRequired()])
    submit = SubmitField('Post')




