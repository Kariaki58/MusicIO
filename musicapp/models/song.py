from musicapp.models.base_model import BaseModel
from musicapp import database
from musicapp.models.favourite import Favourite
from musicapp.models.comment import Comment
from musicapp.models.playlist import Playlist
from musicapp.models.like import Like


class Song(BaseModel, database.Model):
    __tablename__ = 'songs'
    """
    user songs uploads
    """
    title = database.Column(database.String(255), nullable=False)
    artist_name = database.Column(database.String(120), nullable=False, unique=True)
    song_path = database.Column(database.String(255), nullable=False)
    user_id = database.Column(database.Integer, database.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    favourites = database.relationship('Favourite', backref='songs', passive_deletes=True)
    comments = database.relationship('Comment', backref="songs", passive_deletes=True)
    playlist = database.relationship('Playlist', backref='songs', passive_deletes=True)
    likes = database.relationship('Like', backref='songs', passive_deletes=True)
