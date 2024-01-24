from musicapp import database
from musicapp.models.base_model import BaseModel


class Favourite(BaseModel, database.Model):
    __tablename__ = 'favourites'
    """
    models - stores user favourite songs.
    """
    artist_name = database.Column(database.String(120), nullable=False, unique=True)
    song_id = database.Column(database.Integer, database.ForeignKey('songs.id', ondelete='CASCADE'), nullable=False)
    user_id = database.Column(database.Integer, database.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)