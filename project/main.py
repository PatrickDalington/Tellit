from flask import Blueprint, render_template, request, redirect, url_for, flash, current_app, Flask, jsonify
from .models import Story, Images
from . import db, create_app
from .models import User
import requests
import secrets
import os
from flask_login import login_required, current_user
# from flask_imgur import Imgur
from imgurpython import ImgurClient

app = Flask(__name__)

main = Blueprint('main', __name__, template_folder='templates', static_folder='static')

# main.config["IMGUR_ID"] = "8ec1ebd4fb56477"
# imgur_handler = Imgur(main)


UPLOAD_FOLDER = 'project/static/images/'
with app.app_context():
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Configuration for Imgur API
IMGUR_CLIENT_ID = '8ec1ebd4fb56477'
IMGUR_CLIENT_SECRET = 'f9d8f1b2d5267591649075da4a8069627a7f9402'
IMGUR_ACCESS_TOKEN = 'e58bf8d0d887e31fe724f4d1e4ad07d82bc8d591'
IMGUR_REFRESH_TOKEN = '7b4d8ac8e6ba333ce91e800689ef20ebfbf6dfff'

SESSION_REFRESH_EACH_REQUEST = True


def upload_to_imgur(image_path):
    client = ImgurClient(IMGUR_CLIENT_ID, IMGUR_CLIENT_SECRET, IMGUR_ACCESS_TOKEN, IMGUR_REFRESH_TOKEN)
    response = client.upload_from_path(image_path, anon=True)
    return response['link']


@main.route('/upload_')
def upload_():
    return render_template('upload.html')


@main.route('/upload', methods=['GET', 'POST'])
def upload_image():
    if request.method == 'POST':
        image = request.files['file']
        if image.filename != '':
            image_path = os.path.join(app.config['UPLOAD_FOLDER'], image.filename)
            image.save(image_path)
            img_link = upload_to_imgur(image_path)

            new_image = Images(image=img_link)
            db.session.add(new_image)
            db.session.commit()

            return redirect(url_for('main.success'))

    return render_template('upload.html')


@main.route('/')
def index():
    all_user_stories = Story.query.all()
    # mStory = [i for i in all_user_stories]
    mStory = []
    mActionStory = []
    mFantasyStory = []

    # Generating random number of script for UI beautification
    import random

    # STORIES FOR THE WEEK [ VIEW MAXIMUM OF 5 STORIES]
    max_stories_for_the_week = 0
    for i in all_user_stories:
        if max_stories_for_the_week < 10:
            mStory.append(i)
        max_stories_for_the_week += 1

    # TRENDING ACTION STORIES [ VIEW MAXIMUM OF 5 STORIES]
    max_action_stories_ = 0
    for i in all_user_stories:
        if i.story_category == 'Action':
            if max_action_stories_ < 5:
                mActionStory.append(i)
            max_action_stories_ += 1

    # TRENDING FANTASY STORIES [ VIEW MAXIMUM OF 5 STORIES]
    max_fantasy_stories_ = 0
    for i in all_user_stories:
        if i.story_category == 'Fantasy':
            if max_fantasy_stories_ < 5:
                mFantasyStory.append(i)
            max_fantasy_stories_ += 1

    # Shuffle story list
    random.shuffle(mStory)
    random.shuffle(mActionStory)

    return render_template('index.html', mStory=mStory, mActionStory=mActionStory, mFantasyStory=mFantasyStory,
                           random=random)


@main.route('/reader/<post_id>', methods=('GET', 'POST'))
def reader(post_id):
    mStory = []
    featureStory = []
    category = ''

    if request.method == 'POST':

        read = request.form['read']

        all_user_stories = Story.query.all()
        for i in all_user_stories:
            if i.post_id == read:
                category = i.story_category
                mStory.append(i)

        # Loading feature stories on readers page [ VIEW MAXIMUM OF 5 STORIES]
        max_featured_stories_ = 0
        for i in all_user_stories:
            if i.story_category == category:
                if max_featured_stories_ < 5 and i.post_id != read:
                    featureStory.append(i)
                max_featured_stories_ += 1

        # mStory = [i for i in all_user_stories]
        # mStory = Story.query.filter_by(post_id=read).first()

    return render_template('story_reader.html', mStory=mStory, featureStory=featureStory)


@main.route('/add', methods=('GET', 'POST'))
@login_required
def create():
    if request.method == 'POST':
        post_id = secrets.token_urlsafe(16)
        poster_id = current_user.user_id
        title = request.form['title']
        caption = request.form['caption']
        content = request.form['content']
        image = request.form['image']
        part = request.form['part']
        character = request.form['character']
        category = request.form.get('category')
        audience = request.form.get('audience')
        copyright = request.form.get('copyright')

        f_name = current_user.first_name
        l_name = current_user.last_name

        # Validating information from form
        if not title:
            flash('Please enter title')
        if not caption:
            flash('Please enter caption')
        if not content:
            flash('Please enter content')
        if not image:
            flash('Please enter image url')
        if not part:
            flash('Please enter the part of the story [example; part 1, part 2 ...]')
        if not category or category == 'Choose':
            flash('Please choose category')
        if not audience or audience == 'Choose':
            flash('Please choose preferred audience')
        if not copyright or copyright == 'Choose':
            flash('Please choose copyright')
        else:

            story = Story(post_id=post_id, poster_fist_name=f_name, poster_last_name=l_name, poster_id=poster_id,
                          title=title,
                          caption=caption, content=content, image=image,
                          story_part=part.capitalize(), main_characters=character, story_category=category,
                          story_audience=audience, story_copyright=copyright)
            db.session.add(story)
            db.session.commit()
            success = 'success'

            return redirect(url_for('main.success'))

    story_cat = ['Choose', 'Romance', 'Love', 'Tragedy', 'Action', 'Adventure', 'Fanfiction', 'Fantasy',
                 'General Fiction', 'Horror', 'Humor', 'Mystery/Thriller', 'Non-Fiction', 'Paranormal',
                 'Poetry', 'Random', 'Science Fiction', 'Short Story', 'Spiritual', 'WereWolf', 'Teen Fiction',
                 'Vampire']
    story_aud = ['Choose', 'Young Adult (13-18 years of age)', 'New Adult (18-25 years of age)',
                 'Adult (25+ years of age)']
    story_copyright = ['Choose', 'All Right Reserved', 'Public Domain']

    return render_template('add.html', story_cat=story_cat, story_aud=story_aud, story_copyright=story_copyright)


@main.route('/all-best-stories/')
def all_best_stories():
    al_best_stories = Story.query.all()

    # Generating random number of script for UI beautification
    import random

    # STORIES FOR THE WEEK [ VIEW ALL BEST STORIES]
    mStory = [i for i in al_best_stories]

    # Shuffle story list
    random.shuffle(mStory)

    return render_template('best_stories.html', mStory=mStory)


@main.route('/all-action-stories/')
def all_action_stories():
    al_action_stories = Story.query.all()

    # Generating random number of script for UI beautification
    import random

    # STORIES FOR THE WEEK [ VIEW ALL BEST STORIES]
    mStory = [i for i in al_action_stories]

    # Shuffle story list
    random.shuffle(mStory)

    return render_template('action_stories.html', mStory=mStory)


@main.route('/all-movie-script/')
def all_movie_script():
    al_movie_script = Story.query.all()

    # Generating random number of script for UI beautification
    import random

    # STORIES FOR THE WEEK [ VIEW ALL BEST STORIES]
    mScript = [i for i in al_movie_script]

    # Shuffle story list
    random.shuffle(mScript)

    return render_template('movie_script.html', mScript=mScript)


@main.route('/success/')
def success():
    return render_template('success.html')


@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user)


