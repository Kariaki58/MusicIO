from musicapp.models.base_model import BaseModel
from musicapp import database


class Playlist(BaseModel, database.Model):
    __tablename__ = 'playlists'
    """
    playlist database.
    """
    title = database.Column(database.String(120), nullable=False, unique=True)
    artist_name = database.Column(database.String(120), nullable=False)
    playlist_name = database.Column(database.String(120), nullable=False, unique=True)
    songs = database.relationship('Song', backref='playlist', passive_deletes=True)
    user_id = database.Column(database.Integer, database.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
