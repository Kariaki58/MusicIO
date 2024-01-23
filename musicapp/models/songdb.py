from musicapp.models.dbmodels import BaseModel
from musicapp import database


class Song(BaseModel):
    """
    user songs uploads
    """
    title = database.Column(database.String(255), nullable=False)
    artist_name = database.Column(database.String(120), nullable=False, unique=True)
    song_path = database.Column(database.String(255), nullable=False)
    user_id = database.Column(database.Integer, database.ForeignKey('user.id', ondelete='CASCADE', useexisting=True), nullable=False)
    favourites = database.relationship('Favourite', backref='song', passive_deletes=True)
    comments = database.relationship('Comment', backref="song", passive_deletes=True)
    playlist = database.relationship('Playlist', backref='song', passive_deletes=True)
    likes = database.relationship('Like', backref='song', passive_deletes=True)
