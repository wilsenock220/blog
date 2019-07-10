from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, PasswordField,SelectField
from wtforms.validators import Required
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField
from wtforms import ValidationError
from wtforms.validators import Required,Email,EqualTo,DataRequired
from ..models import User

class RegistrationForm(FlaskForm):
    email = StringField('Your Email Address',validators=[Required(),Email()])
    username = StringField('Enter your username',validators = [Required()])
    password = PasswordField('Password',validators = [Required(), EqualTo('password_confirm',message = 'Passwords must match')])
    password_confirm = PasswordField('Confirm Passwords',validators = [Required()])
    subscribe = SelectField(' Would like to an email alert when a new post is made ', coerce=int,
            choices=[(0, 'Please Select an option...'), (1, 'Yes'),(2, 'No')],
            validators = [Required()])
    role = SelectField(' Select Role ', coerce=int,
            choices=[(0, 'Please Select a role...'), (1, 'Writer'),(2, 'User')],
            validators = [Required()])
    submit = SubmitField('Sign Up')

    def validate_email(self,data_field):
                if User.query.filter_by(email =data_field.data).first():
                    raise ValidationError('There is an account with that email')

    def validate_username(self,data_field):
            if User.query.filter_by(username = data_field.data).first():
                raise ValidationError('That username is taken')


class LoginForm(FlaskForm):
    email = StringField('Your Email Address',validators=[Required(),Email()])
    password = PasswordField('Password',validators =[Required()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign In')