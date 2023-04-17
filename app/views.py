from datetime import datetime
import os
from app import app, db
from flask import Flask, jsonify, make_response, redirect, request, send_from_directory, session, url_for
from flask_cors import CORS, cross_origin
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token



from werkzeug.utils import secure_filename

from app.forms import *
from flask_wtf.csrf import generate_csrf

from app.models import *

###
# Routing for your application.
###






@app.route('/api/v1/register', methods =["POST"])
def register():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        firstname = form.firstname.data
        lastname = form.lastname.data
        email = form.email.data
        location = form.location.data
        biography = form.biography.data
        profile_photo = form.profile_photo.data
        filename = secure_filename(profile_photo.filename)
        profile_photo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        

        # Check if the username is already taken
        if User.query.filter_by(username=username).first() is not None:
            response = {
                'errors': 'Username already taken'
            }
            return jsonify(response), 400

        # Check if the email is already taken
        if User.query.filter_by(email=email).first() is not None:
            response = {
                'errors': 'Email already taken'
            }
            return jsonify(response), 400

        # Create a new user instance
        user = User(
            username=username,
            password=password,
            firstname=firstname,
            lastname=lastname,
            email=email,
            location=location,
            biography=biography,
            profile_photo=filename,
            joined_on=datetime.now()
        )

        # Add the user to the database
        db.session.add(user)
        db.session.commit()

        
        response = {
            'message': 'User successfully registered',
            'id': user.id,
            'username': user.username,
            'firstname': user.firstname,
            'lastname': user.lastname,
            'email': user.email,
            'location': user.location,
            'biography': user.biography,
            'profile_photo': user.profile_photo,
            'joined_on': user.joined_on
        }
        return jsonify(response), 201

    errors = form_errors(form)
    response = {'errors':errors}
    print(response)
    return jsonify(response), 400


@app.route('/api/v1/auth/login', methods=['POST'])
def login():
    form = LoginForm()

    if request.method == 'POST' and form.validate_on_submit():
        # Get the user's login credentials
        username = form.username.data
        password = form.password.data

        # Try to find the user by their username in the database
        user = User.query.filter_by(username=username).first()

        # If the user is found and their password is correct, log them in
        if user is not None and user.check_password(password):
            response = {
                'message': 'Login successful',
                'id': user.id,
                'username': user.username,
                'firstname': user.firstname,
                'lastname': user.lastname,
                'email': user.email,
                'location': user.location,
                'biography': user.biography,
                'profile_photo': user.profile_photo,
                'joined_on': user.joined_on,
                'access_token': create_access_token(identity=user.id)
            }
            
            return jsonify(response), 200

        # If the user is not found or their password is incorrect, return an error message
        response = {
            'errors': 'Invalid credentials'
        }
        return jsonify(response), 401

    errors = form_errors(form)
    response = {'errors': errors}
    return jsonify(response), 400


@app.route('/api/v1/auth/logout', methods=['POST'])
def logout():
   
    response = {
        'message': 'Logout successful'
    }
    return jsonify(response), 200

@app.route('/api/v1/users/<int:user_id>/posts', methods=['POST'])
@jwt_required()
def create_post(user_id):

    form = PostForm()
    current_user = get_jwt_identity()


    if current_user == user_id:
        if request.method == 'POST' and form.validate_on_submit():
            caption = form.caption.data
            photo = form.photo.data
            filename = secure_filename(photo.filename)
            photo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))        

            # Check if user exists
            user = User.query.get(user_id)
            if user is None:
                response = {
                    'errors': 'User not found'
                }
                return jsonify(response), 404

            # Create a new post instance
            post = Post(
                user_id=user_id,
                caption=caption,
                photo=filename,
                created_on=datetime.now()
            )

            # Add the post to the database
            db.session.add(post)
            db.session.commit()

            response = {
                'message': 'Post successfully created',
                'id': post.id,
                'user_id': post.user_id,
                'caption': post.caption,
                'photo': post.photo,
                'posted_on': post.created_on
            }
            return jsonify(response), 201
    else:
        return redirect(url_for('login'))
    errors = form_errors(form)
    response = {'errors': errors}
    return jsonify(response), 400


@app.route('/api/v1/users/<int:user_id>/posts', methods=['GET'])
@jwt_required()
def get_user_posts(user_id):
    # Check if user exists
    user = User.query.filter_by(id=user_id).first()
    if not user:
        response = {
            'errors': 'User not found'
        }
        return jsonify(response), 404

    # Serialize the user
    serialized_user = {
        'first_name': user.firstname,
        'last_name': user.lastname,
        'location': user.location,
        'joined_on': user.joined_on.strftime('%b %Y'),
        'biography': user.biography,
        'profile_photo': url_for('get_photo', filename=user.profile_photo, _external=True)
    }

    user_follows = Follow.query.filter_by(user_id=user_id).all()
    serialized_follows = []
    for follow in user_follows:
        serialized_follows.append({
            'id': follow.id,
            'user_id': follow.user_id,
            'follower_id' : follow.follower_id
        })


    # Get user's posts
    user_posts = Post.query.filter_by(user_id=user_id).all()

    # Serialize the posts to JSON
    serialized_posts = []
    for post in user_posts:
        serialized_posts.append({
            'id': post.id,
            'user_id': post.user_id,
            'photo_url': url_for('get_photo', filename=post.photo, _external=True),
            'caption': post.caption,
            'created_on': post.created_on
        })

    # Return the serialized user and posts
    response = {
        'user': serialized_user,
        'posts': serialized_posts,
        'follows': serialized_follows
    }
    return jsonify(response), 200



@app.route('/api/v1/users/<int:user_id>/follow', methods=['POST'])
@jwt_required()
def follow_user(user_id):
    current_user_id = get_jwt_identity()
    user_to_follow = User.query.get(user_id)
    
    if not user_to_follow:
        return jsonify({'message': 'User not found'}), 404
    
    if current_user_id == user_id:
        return jsonify({'message': 'You cannot follow yourself'}), 400
    
    # Check if the user is already being followed
    if Follow.query.filter_by(user_id=user_id, follower_id=current_user_id).first():
        return jsonify({'message': 'You are already following this user'}), 400
    
    # Create a new Follow object and add it to the database
    follow = Follow(user_id=user_id, follower_id=current_user_id)
    db.session.add(follow)
    db.session.commit()
    
    return jsonify({'message': 'You are now following this user'}), 200


@app.route('/api/v1/posts', methods=['GET'])
@jwt_required()
def get_posts():
    # Retrieve all posts from the database
    posts = Post.query.all()
    
    # Create a list to store the serialized posts
    serialized_posts = []

    # Loop through each post and serialize it
    for post in posts:
        likes = post.get_likes()
        serialized_post = {
            'id': post.id,
            'username': post.user.username,
            'user_id': post.user.id,
            'user_photo': url_for('get_photo', filename = post.user.profile_photo, _external = True),
            'caption': post.caption,
            'photo_url': url_for('get_photo', filename=post.photo, _external=True),
            'num_likes': post.num_likes(),
            'likes': likes,
            'created_on': post.created_on.strftime('%d %b %Y')
        }
        serialized_posts.append(serialized_post)

    # Return the serialized posts as JSON
    return jsonify(serialized_posts), 200


@app.route('/api/v1/posts/<int:post_id>/like', methods=['POST'])
@jwt_required()
def like_post(post_id):
    current_user_id = get_jwt_identity()
    # Get the post
    post = Post.query.get(post_id)

    # Check if the post exists
    if post is None:
        response = {
            'message': 'Post not found'
        }
        return jsonify(response), 404

   
    # Check if the user has already liked the post
    if Like.query.filter_by(user_id=current_user_id, post_id=post_id).first() is not None:
        response = {
            'message': 'User has already liked this post'
        }
        return jsonify(response), 400

    # Create a new like instance
    like = Like(
        user_id=current_user_id,
        post_id=post_id    
    )

    # Add the like to the database
    db.session.add(like)
    db.session.commit()

    response = {
        'message': 'Post liked successfully'
    }
    return jsonify(response), 201


# @app.route('/')
# def index():
#     session['username'] = 'John'
#     return 'Session data set'

# @app.route('/pop')
# def pop_sess():
#     session.pop('username', None)
#     return 'Session popped'

# @app.route('/get_session')
# def get_ses():
#     username = session.get('user_id')
#     return f'The username is {username}'



@app.route('/api/v1/posters/<filename>')
def get_photo(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/api/v1/site/<filename>')
def get_site_img(filename):
    return send_from_directory(app.config['ASSESTS_FOLDER'], filename)

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,access-control-allow-origin')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    response.headers.add('Access-Control-Allow-Credentials', 'true')
    return response

@app.route('/')
def index():
    return jsonify(message="This is the beginning of our API")


###
# The functions below should be applicable to all Flask apps.
###

# Here we define a function to collect form errors from Flask-WTF
# which we can later use

def form_errors(form):
    error_messages = []
    """Collects form errors"""
    for field, errors in form.errors.items():
        for error in errors:
            message = u"Error in the %s field - %s" % (
                    getattr(form, field).label.text,
                    error
                )
            error_messages.append(message)
    return error_messages



@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(401)
def unauthorized(error):
    # This error handler is called when a user tries to access a protected page without being authenticated
    return redirect(url_for('login', error='You must be logged in to access this page'))  # redirect to login page with error message in query parameter

@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return jsonify(message=f"{error}"), 404


@app.route('/api/v1/csrf-token', methods=['GET'])
def get_csrf():
    return jsonify({'csrf_token': generate_csrf()})
