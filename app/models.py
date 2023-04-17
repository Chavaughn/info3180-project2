from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from . import db
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    password = db.Column(db.String(128))
    firstname = db.Column(db.String(50))
    lastname = db.Column(db.String(50))
    email = db.Column(db.String(120))
    location = db.Column(db.String(50))
    biography = db.Column(db.String(500))
    profile_photo = db.Column(db.String(200))
    joined_on = db.Column(db.DateTime)

    def __init__(self, username, password, firstname, lastname, email, location, biography, profile_photo, joined_on):
        self.username = username
        self.password = generate_password_hash(password, method='pbkdf2:sha256')
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.location = location
        self.biography = biography
        self.profile_photo = profile_photo
        self.joined_on = joined_on

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'firstname': self.firstname,
            'lastname': self.lastname,
            'email': self.email,
            'location': self.location,
            'biography': self.biography,
            'profile_photo': self.profile_photo,
            'joined_on': self.joined_on.strftime('%Y-%m-%d %H:%M:%S')
        }

class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    caption = db.Column(db.String(500))
    photo = db.Column(db.String(200))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    created_on = db.Column(db.DateTime)
    user = db.relationship('User', backref='posts')
    liked_by = db.relationship('Like', backref='posts', lazy='dynamic')

    def __init__(self, caption, photo, user_id, created_on):
        self.caption = caption
        self.photo = photo
        self.user_id = user_id
        self.created_on = created_on

    def num_likes(self):
        return self.liked_by.count()

    def get_likes(self):
        return [like.user_id for like in self.liked_by]


class Like(db.Model):
    __tablename__ = 'likes'
    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    post = db.relationship('Post', backref='likes')
    user = db.relationship('User', backref='likes')

    def __init__(self, post_id, user_id):
        self.post_id = post_id
        self.user_id = user_id

    def to_dict(self):
        return {
            'id': self.id,
            'user': self.user.to_dict(),
        }


class Follow(db.Model):
    __tablename__ = 'follows'
    id = db.Column(db.Integer, primary_key=True)
    follower_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    
    def __init__(self, follower_id, user_id):
        self.follower_id = follower_id
        self.user_id = user_id