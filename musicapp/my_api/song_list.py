from . import my_api_views
from flask_login import LoginManager
from flask import jsonify, request
from werkzeug.utils import secure_filename
import os
from musicapp import database, login_manager


@my_api_views.route('/<int:playlist_id>/songs', methods=['GET'])
def get_songs(playlist_id):
    from musicapp.models.song import Song
    songs = Song.query.filter(Song.playlist_id==playlist_id).all()
    song_content_with_playlist = []
    for song in songs:
        song_dict = song.to_dict()
        song_dict.pop('_sa_instance_state')
        song_content_with_playlist.append(song_dict)
    return jsonify(song_content_with_playlist)