from musicapp import database
from musicapp.models.like import Like
from musicapp.models.song import Song
from musicapp.models.user import User
from musicapp.models.comment import Comment
from musicapp.models.favourite import Favourite
from musicapp.models.playlist import Playlist


from musicapp.run import app


if  app:
    user = User(email="jjj@gmaddskl.c", password="1323", username="cory")

    song = Song(title="fire masnxxy", artist_name="asndrew tate v2", song_path="~/home/dirfd", user=user)
    user_q = User.query.all()

    print(user_q)
    comment = Comment(text="hey i hate you favour", user=user, song=song)
    playlist = Playlist(title="My best music", user=user, songs=song)

    database.session.add(user)
    database.session.add(song)
    database.session.add(comment)
    database.session.add(playlist)

    database.session.commit()
