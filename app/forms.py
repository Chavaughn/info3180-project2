from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField,  FileField
from wtforms.validators import DataRequired
from flask_wtf.file import  FileAllowed , FileRequired


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    firstname = StringField('First Name', validators=[DataRequired()])
    lastname = StringField('Last Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    biography = StringField('Biography', validators=[DataRequired()])
    profile_photo = FileField('Profile Photo', validators=[FileRequired(), FileAllowed(['jpg', 'png', 'jpeg'], 'Images only!')])
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class PostForm(FlaskForm):
    caption = StringField('Caption', validators=[DataRequired()])
    photo = StringField('Photo URL', validators=[DataRequired()])
    submit = SubmitField('Submit')

class LikeForm(FlaskForm):
    submit = SubmitField('Like')

class FollowForm(FlaskForm):
    submit = SubmitField('Follow')