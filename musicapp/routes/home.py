from flask import (
    Flask, Blueprint, render_template, jsonify, request, redirect, flash,
    jsonify
)
from werkzeug.utils import secure_filename
from flask_login import current_user, login_required
import os


home = Blueprint("home", __name__)

def allowed_file(filename):
    from musicapp.run import app
    if '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']:
        return True
    return False


def handle_user_form(title, artist_name, file):
    from musicapp.run import app
    from musicapp.models.playlist import Playlist
    from musicapp.models.user import User
    from musicapp.models.song import Song
    from musicapp import database

    app_user = current_user.get_id()
    if app_user is None:
        return False

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)

        try:
            os.mkdir(app.config['UPLOAD_FOLDER'])
        except FileExistsError:
            pass

        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        
        file.save(filepath)

        new_filename = f'{title}.mp3'
        new_filename = new_filename.replace(' ', '_')

        new_filepath = os.path.join(app.config['UPLOAD_FOLDER'], new_filename)
        os.rename(filepath, new_filepath)
        playlist_query = Playlist.query.filter(Playlist.user_id==app_user).first()
        playlist_is_valid = playlist_query is None

        if playlist_is_valid:
            new_playlist = Playlist(title=title, user_id=app_user)
            database.session.add(new_playlist)
            song_path = f'{app.config["UPLOAD_FOLDER"]}/{new_filename}'
            database.session.commit()
            new_song = Song(title=title, artist_name=artist_name, user_id=app_user, playlist_id=new_playlist.id, song_path=new_filepath)
            database.session.add(new_song)
            database.session.commit()
            return True
        
        new_song = Song(title=title, artist_name=artist_name, user_id=app_user, playlist_id=playlist_query.id, song_path=new_filepath)
        database.session.add(new_song)
        database.session.commit()
    
    return True

def user_input_validation(title, artist_name):
    """
    This ensures that song title are not the same
    """
    from musicapp.models.song import Song
    from musicapp.models.user import User


    songs = Song.query.filter(Song.title==title).first()
    if songs:
        return True
    return False


@home.route('/', methods=['GET', 'POST'])
def home_page():
    from musicapp.models.playlist import Playlist
    from musicapp.models.song import Song

    title = request.form.get('title')
    artist_name = request.form.get('artist_name')
    file = request.files.get('file')
    content_list = []

    if request.method == 'POST':
        error = False
        if user_input_validation(title, artist_name):
            error = {
                'error': 'title already exist'
            }
            return jsonify(error)
        
        elif not handle_user_form(title, artist_name, file):
            error = True
            flash('you are not logedin')

        if error:
            return redirect('login')
        
    playlist = Playlist.query.all()
    for data in playlist:
        playlists = data.to_dict()
        playlists.pop('_sa_instance_state', None)
        content_list.append(playlists)
    print('reached this point')
    return render_template('home.html', content_list=content_list, id="don't use js")
