from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField,TextAreaField,SelectField
from wtforms.validators import Required
from ..models import Blog

class BlogForm(FlaskForm):
    blog_title = StringField('Blog title',validators=[Required()])
    blog = TextAreaField('Blog',validators=[Required()])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    comment = TextAreaField('comment',validators=[Required()])
    submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')

