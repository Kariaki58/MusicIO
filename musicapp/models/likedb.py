from musicapp import database
from musicapp.models.dbmodels import BaseModel


class Like(BaseModel):
    __tablename__ = 'like_table'
    user_id = database.Column(database.Integer, database.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    song_id = database.Column(database.Integer, database.ForeignKey('song.id', ondelete='CASCADE'), nullable=False)
