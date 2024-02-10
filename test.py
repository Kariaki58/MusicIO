from musicapp import database
from musicapp.models.like import Like
from musicapp.models.song import Song
from musicapp.models.user import User
from musicapp.models.comment import Comment
from musicapp.models.favourite import Favourite
from musicapp.models.playlist import Playlist


from musicapp.run import app


if  app:
    user = User(email="jjj@gmaddskl.com", password="1323", username="cory123")

    song = Song(title="Calm down", artist_name="Rema", song_path="~/home/dirfds", user=user)
    user_q = User.query.all()

    print(user_q)
    comment = Comment(text="Best afro", user=user, song=song)
    playlist = Playlist(title="Afro", user=user, songs=[song])

    database.session.add(user)
    database.session.add(song)
    database.session.add(comment)
    database.session.add(playlist)

    database.session.commit()
