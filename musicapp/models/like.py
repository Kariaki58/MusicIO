from musicapp import database
from musicapp.models.base_model import BaseModel


class Like(BaseModel, database.Model):
    __tablename__ = 'likes'
    user_id = database.Column(database.Integer, database.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    song_id = database.Column(database.Integer, database.ForeignKey('songs.id', ondelete='CASCADE'), nullable=False)
