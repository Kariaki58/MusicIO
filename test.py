from musicapp import database
from musicapp.models.likedb import Like
from musicapp.models.songdb import Song
from musicapp.models.userdb import User
from musicapp.models.commentdb import Comment
from musicapp.models.favouritedb import Favourite
from musicapp.models.playlist import Playlist


from run import app


if app:
    user = User(email="jjj@gmaddskl.c", password="1323", username="cory")

    song = Song(title="fire masnxxy", artist_name="asndrew tate v2", song_path="~/home/dirfd", user=user)
    user_q = User.query.all()

    print(user_q)
    comment = Comment(text="hey i hate you favour", user_id=user.id, song_id=1)
    playlist = Playlist(title="My best music", user_id=user.id, song_id=1)

    database.session.add(user)
    database.session.add(song)
    database.session.add(comment)
    database.session.add(playlist)

    database.session.commit()