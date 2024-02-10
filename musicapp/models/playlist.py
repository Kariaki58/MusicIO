from musicapp.models.base_model import BaseModel
from musicapp import database


playlist_songs = database.Table('playlist_songs',
        database.Column('id', database.Integer, primary_key=True),
        database.Column('playlist_id', database.Integer, database.ForeignKey('playlists.id')),
        database.Column('song_id', database.Integer, database.ForeignKey('songs.id'))
        )

class Playlist(BaseModel, database.Model):
    __tablename__ = 'playlists'
    """
    user songs uploads
    """
    title = database.Column(database.String(120), nullable=False, unique=True)
    songs = database.relationship('Song', backref='playlist', passive_deletes=True)
    user_id = database.Column(database.Integer, database.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    songs = database.relationship('Song', secondary = 'playlist_songs', back_populates = 'playlists')
    # do not uncomment this. still under testing
    # song_id = database.Column(database.Integer, database.ForeignKey('songs.id', ondelete='CASCADE'), nullable=False)
