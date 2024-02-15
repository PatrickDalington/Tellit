from . import db
from flask_login import UserMixin
import datetime
import secrets


class User(UserMixin, db.Model):
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(16), unique=True)
    first_name = db.Column(db.String(25))
    last_name = db.Column(db.String(25))
    phone = db.Column(db.String(20))
    username = db.Column(db.String(15), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(80))
    imageUrl = db.Column(db.Text, unique=True, nullable=True)
    imageName = db.Column(db.String(), nullable=False)


class Story(db.Model):
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.String(16))
    poster_fist_name = db.Column(db.String())
    poster_last_name = db.Column(db.String())
    poster_id = db.Column(db.String())
    title = db.Column(db.String(50), nullable=False)
    content = db.Column(db.Text)
    caption = db.Column(db.String(50))
    image = db.Column(db.String(150), nullable=False)
    # img_del_id = db.Column(db.String())
    story_part = db.Column(db.String(25))
    main_characters = db.Column(db.String())
    story_category = db.Column(db.String())
    story_audience = db.Column(db.String(20))
    story_copyright = db.Column(db.String())
    created_at = db.Column(db.DateTime(timezone=True), default=datetime.datetime.utcnow)


class Images(db.Model):
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.String())
