from musicapp import database
from musicapp.models.base_model import BaseModel


class Favourite(BaseModel, database.Model):
    """
    models - stores user favourite songs.
    """
    __tablename__ = 'favourites'
    artist_name = database.Column(database.String(120), nullable=False)
    song_path = database.Column(database.String(255), nullable=False)
    song_id = database.Column(database.Integer, database.ForeignKey('songs.id', ondelete='CASCADE'), nullable=False)
    user_id = database.Column(database.Integer, database.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    