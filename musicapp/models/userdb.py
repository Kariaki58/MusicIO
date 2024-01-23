from dbmodels import BaseModel
from flask_login import UserMixin
from musicapp import database


class User(BaseModel, UserMixin):
    """
    user table model
    """
    email = database.Column(database.String(120), unique=True, nullable=False)
    password = database.Column(database.String(10), nullable=False)
    username = database.Column(database.String(120), unique=True, nullable=False)
    playlists = database.relationship('Playlist', backref="user", passive_deletes=True)
    songs = database.relationship('Song', backref='user', passive_deletes=True)
    comments = database.relationship('Comment', backref='user', passive_deletes=True)
    favourites = database.relationship('Favourite', backref='user', passive_deletes=True)
    likes = database.relationship('Like', backref='user', passive_deletes=True)
