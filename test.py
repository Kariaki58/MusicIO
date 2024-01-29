from musicapp import database
from musicapp.models.like import Like
from musicapp.models.song import Song
from musicapp.models.user import User
from musicapp.models.comment import Comment
from musicapp.models.favourite import Favourite
from musicapp.models.playlist import Playlist


from run import app


if app:
    user = User(email="jjjfda2@gmaddskl.c", password="132sdfa32", username="cfdory2")

    song = Song(title="fire masfdanxxy2", artist_name="asndrewfds2 tate v2", song_path="~/hofdsaf2me/dirfd", user=user)
    user_q = User.query.all()

    comment = Comment(text="hey2 sdsafi hate you favour", user=user, song=song)
    playlist = Playlist(title="My2 bessdft music", user=user, songs=song)

    database.session.add(user)
    database.session.add(song)
    database.session.add(comment)
    database.session.add(playlist)

    print("added...")
    database.session.commit()
    print("commemited?")