from . import my_api_views
from flask_login import LoginManager
from flask import jsonify, request
from werkzeug.utils import secure_filename
import os
from musicapp import database, login_manager


@my_api_views.route('/<int:playlist_id>/songs', methods=['POST'])
def get_songs(playlist_id):
    from musicapp.models.song import Song
    from musicapp.models.like import Like
    from musicapp.models.favourite import Favourite

    current_user = request.form.get('user')

    playlistId = request.form.get('playlist_id')

    songs = Song.query.filter(Song.playlist_id == playlist_id).all()

    liked_songs = [like.song_id for like in Like.query.filter(Like.user_id == current_user).all()]
    favourite = [fav.song_id for fav in Favourite.query.filter(Favourite.user_id == current_user).all()]

    song_content_with_playlist = []

    for song in songs:
        song_dict = song.to_dict()
        song_dict['liked'] = 'fa-solid' if song.id in liked_songs else 'fa-regular'
        song_dict["fav"] = 'fa-solid' if song.id in favourite else 'fa-regular'
        song_dict['playlistId'] = playlistId
        song_dict.pop('_sa_instance_state', None)
        song_content_with_playlist.append(song_dict)
    return jsonify(song_content_with_playlist)
