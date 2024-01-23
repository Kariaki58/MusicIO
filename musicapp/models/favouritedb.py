from musicapp import database
from dbmodels import BaseModel


class Favourite(BaseModel):
    """
    models - stores user favourite songs.
    """
    artist_name = database.Column(database.String(120), nullable=False, unique=True)
    song_id = database.Column(database.Integer, database.ForeignKey('song.id', ondelete='CASCADE'), nullable=False)
    user_id = database.Column(database.Integer, database.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
