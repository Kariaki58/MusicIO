from dbmodels import BaseModel
from musicapp import database


class Comment(BaseModel):
    text = database.Column(database.Text, nullable=False)
    user_id = database.Column(database.Integer, database.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    song_id = database.Column(database.Integer, database.ForeignKey('song.id', ondelete='CASCADE'), nullable=False)
