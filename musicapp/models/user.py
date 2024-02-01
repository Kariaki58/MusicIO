from musicapp.models.base_model import BaseModel
from flask_login import UserMixin
from musicapp import database
from werkzeug.security import generate_password_hash, check_password_hash


class User(BaseModel, database.Model, UserMixin):

    __tablename__ = 'users'
    """
    user table model
    """
    email = database.Column(database.String(120), unique=True, nullable=False)
    password = database.Column(database.String(200), nullable=False)
    username = database.Column(database.String(120), unique=True, nullable=False)
    confirm_token = database.Column(database.String(32))
    reset_token = database.Column(database.String(22))
    playlists = database.relationship('Playlist', backref="user", passive_deletes=True)
    songs = database.relationship('Song', backref='user', passive_deletes=True)
    comments = database.relationship('Comment', backref='user', passive_deletes=True)
    favourites = database.relationship('Favourite', backref='user', passive_deletes=True)
    likes = database.relationship('Like', backref='user', passive_deletes=True)


    def __setattr__(self, name, value):
        """sets a password with md5 encryption"""
        if name == "password":
            value = generate_password_hash(value)
        super().__setattr__(name, value)


    def verify_password(self, pwd):
        return check_password_hash(self.password, pwd)

