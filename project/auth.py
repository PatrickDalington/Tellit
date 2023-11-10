from flask import Blueprint, render_template, url_for, redirect, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
import uuid as uuid
import os
from .models import User
from flask_login import login_user, logout_user, login_required
from . import db
import secrets
from base64 import b64encode
import base64
from io import BytesIO

auth = Blueprint('auth', __name__)




@auth.route('/login')
def login():
    return render_template('login.html')


@auth.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False


    user = User.query.filter_by(email=email).first()

    # check if the user actually exists
    # take the user-supplied password, hash it, and compare it to the hashed password in the database
    if not user or not check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login'))  # if the user doesn't exist or password is wrong, reload the page

    # if the above check passes, then we know the user has the right credentials
    login_user(user, remember=remember)
    return redirect(url_for('main.profile'))


@auth.route('/signup')
def signup():
    return render_template('signup.html')


@auth.route('/signup', methods=['POST'])
def signup_post():
    # Starting the signup process
    hashed_password = generate_password_hash(request.form['password'], method='sha256')
    user_id = secrets.token_urlsafe(16)
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    phone = request.form['phone']
    username = request.form['username']
    email = request.form['email']
    password = hashed_password
    profile_pic = request.files['inputFile']


    # Check if its a picture
    if not profile_pic:
        return 'No pic selected', 400
   

    # Grabbing image file name
    pic_filename = secure_filename(profile_pic.filename)

    # Making the image file name unique
    imageName = str(uuid.uuid1()) + "_" + pic_filename

    # Referencing to the original profile pic name to the unique name
    #profile_pic = pic_name


    # Save the actual image
    #profile_pic.save(os.path.join(app.config['UPLOAD_FOLDER']), pic_name)

    # Convert to string to save to database
    


    user = User.query.filter_by(email=email).first() # if this returns a user, then the email already exists in database

    if user: # if a user is found, we want to redirect back to signup page so user can try again  
        flash('Email address already exists')
        return redirect(url_for('auth.signup'))

    new_user = User(user_id=user_id, first_name=first_name, last_name=last_name,
                    phone=phone, username=username, email=email,
                    password=password, imageUrl=profile_pic.read(), imageName=imageName)

    # Otherwise,
    # Adding new user to database
    db.session.add(new_user)
    db.session.commit()
    return redirect(url_for('auth.login'))


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))


def render_picture(data):
    render_pic = base64.b64encode(data).decode('ascii')
    return render_pic
