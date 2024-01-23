from musicapp.models.dbmodels import BaseModel
from musicapp import database


class Playlist(BaseModel):
    """
    user songs uploads
    """
    tilte = database.Column(database.String(120), nullable=False, unique=True)
    user_id = database.Column(database.Integer, database.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    song_id = database.Column(database.Integer, database.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
