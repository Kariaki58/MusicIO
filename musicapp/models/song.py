from musicapp.models.base_model import BaseModel
from musicapp import database


class Song(BaseModel, database.Model):
    __tablename__ = 'songs'
    """
    user songs uploads
    """
    title = database.Column(database.String(255), nullable=False, unique=True)
    artist_name = database.Column(database.String(120), nullable=False)
    song_path = database.Column(database.String(255), nullable=False)
    user_id = database.Column(database.Integer, database.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    playlist_id = database.Column(database.Integer, database.ForeignKey('playlists.id', ondelete='CASCADE'), nullable=False)
    favourites = database.relationship('Favourite', backref='songs', passive_deletes=True)
    comments = database.relationship('Comment', backref="song", passive_deletes=True)
    likes = database.relationship('Like', backref='songs', passive_deletes=True)
