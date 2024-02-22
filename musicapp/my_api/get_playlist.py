from . import my_api_views
from flask_login import LoginManager
from flask import jsonify, request
from werkzeug.utils import secure_filename
import os
from musicapp import database


def allowed_file(filename):
    from musicapp.run import app
    if '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']:
        return True
    return False


def handle_user_form(title, artist_name, playlist_name, file, user):
    from musicapp.run import app
    from musicapp.models.playlist import Playlist
    from musicapp.models.user import User
    from musicapp.models.song import Song


    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        folder_parent = 'musicapp'
        parent_child = 'static'
        try:
            path = os.path.join(folder_parent, parent_child, app.config['UPLOAD_FOLDER'])
            os.mkdir(path)
        except FileExistsError:
            pass
        filepath = os.path.join(folder_parent, parent_child, app.config['UPLOAD_FOLDER'], filename)

        file.save(filepath)

        new_filename = f'{title}.mp3'
        new_filename = new_filename.replace(' ', '_')

        new_filepath = os.path.join(folder_parent, parent_child, app.config['UPLOAD_FOLDER'], new_filename)
        os.rename(filepath, new_filepath)
        playlist_query = Playlist.query.filter(Playlist.user_id==user).first() # create only one playlist.
        playlist_is_valid = playlist_query is None
        song_path = f'{app.config["UPLOAD_FOLDER"]}/{new_filename}'
        if playlist_is_valid:
            new_playlist = Playlist(title=title, artist_name=artist_name, playlist_name=playlist_name, user_id=user)
            database.session.add(new_playlist)
            database.session.commit()
            new_song = Song(title=title, user_id=user, playlist_id=new_playlist.id, song_path=song_path)
            database.session.add(new_song)
            database.session.commit()
        else:
            new_song = Song(title=title, user_id=user, playlist_id=playlist_query.id, song_path=song_path)
            database.session.add(new_song)
            database.session.commit()


def user_input_validation(title, playlist_name):
    from musicapp.models.song import Song
    from musicapp.models.playlist import Playlist
    
    songs = Song.query.filter(Song.title==title).first()
    playlists = Playlist.query.filter(Playlist.playlist_name==playlist_name).first()

    if songs is not None:
        return "song"
    
    if playlists is not None:
        return "playlist"
    
    return True


def query_playlist():
    from musicapp.models.playlist import Playlist

    content_list = []
    playlist = Playlist.query.all()
    for data in playlist:
        playlists = data.to_dict()
        playlists.pop('_sa_instance_state', None)
        content_list.append(playlists)
    return content_list


@my_api_views.route("/playlist", methods=['GET'])
def get_playlist():
    from musicapp.models.playlist import Playlist
    
    content_list = query_playlist()
    return jsonify(content_list)


@my_api_views.route('/playlist', methods=['POST'])
def insert_playlist_to_db():
    from musicapp.models.song import Song

    file = request.files['fileInput']

    title = request.form.get('title')
    artist_name = request.form.get('artistName')
    playlist_name = request.form.get('playlistName')
    user = request.form.get('user')
    
    print(file)
    print(title)
    print(artist_name)
    print(playlist_name)
    print(user)
    user_validate = user_input_validation(title, playlist_name)
    if user_validate == "song":
        return jsonify({'message': 'Song name already exist'})
    elif user_validate == "playlist":
        return jsonify({'message': 'Playlist name already exist'})
    handle_user_form(title, artist_name, playlist_name, file, user)
    
    return jsonify({'message': 'upload success', 'playlist_name': True})
