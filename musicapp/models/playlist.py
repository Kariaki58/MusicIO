from musicapp.models.base_model import BaseModel
from musicapp import database


class Playlist(BaseModel, database.Model):
    __tablename__ = 'playlists'
    """
    user songs uploads
    """
    title = database.Column(database.String(120), nullable=False, unique=True)
    songs = database.relationship('Song', backref='playlist', passive_deletes=True)
    user_id = database.Column(database.Integer, database.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    # do not uncomment this. still under testing
    # song_id = database.Column(database.Integer, database.ForeignKey('songs.id', ondelete='CASCADE'), nullable=False)
