from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, Length, Regexp
from flask_wtf.file import FileField, FileAllowed

class MovieForm(FlaskForm):
    title = StringField('Movie Title', validators=[
        DataRequired(message='Please enter the movie title.'),
        Length(min=1, max=100, message='Movie title must be between 1 and 100 characters.'),
    ])
    description = TextAreaField('Description', validators=[
        DataRequired(message='Please enter a brief description or summary of the movie.'),
        Length(min=10, max=500, message='Description must be between 10 and 500 characters.')
    ])
    poster = FileField('Movie Poster', validators=[
        FileAllowed(['jpg', 'jpeg', 'png'], message='Only JPEG, JPG, and PNG images are allowed.')
    ])
