from musicapp.models.base_model import BaseModel
from musicapp import database


class Comment(BaseModel, database.Model):
    """
    comment database
    """
    __tablename__ = 'comments'

    text = database.Column(database.Text, nullable=False)
    user_id = database.Column(database.Integer, database.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    song_id = database.Column(database.Integer, database.ForeignKey('songs.id', ondelete='CASCADE'), nullable=False)
