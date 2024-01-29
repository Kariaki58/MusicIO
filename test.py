from musicapp import database
from musicapp.models.like import Like
from musicapp.models.song import Song
from musicapp.models.user import User
from musicapp.models.comment import Comment
from musicapp.models.favourite import Favourite
from musicapp.models.playlist import Playlist
from run import app


if app:
    user = User.query.first()
    song = Song.query.offset(1).first()
    # song = Song(title="fire masfdanxxy2", artist_name="asndrewfds2 tate v2", song_path="~/hofdsaf2me/dirfd", user=user)
    # user_q = User.query.all()
    print(song.id)
    comment = Comment(text="Hello world", user_id=user.id, song_id=song.id)
    # playlist = Playlist(title="My2 bessdft music", user=user, songs=song)

    # database.session.add(user)
    # database.session.add(song)
    database.session.add(comment)
    # database.session.add(playlist)

    print("added...")
    database.session.commit()
    print("commemited?")
