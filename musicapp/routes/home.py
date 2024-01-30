from flask import Flask, Blueprint, render_template, jsonify


home = Blueprint("home", __name__)


@home.route('/', methods=['GET'])
def home_page():
    from musicapp.models.playlist import Playlist
    content_list = []
    playlist = Playlist.query.all()
    for playlists in playlist:
        playlist_dict = song.to_dict()
        song_dict.pop('_sa_instance_state', None)
        content_list.append(song_dict)

    return jsonify(content_list)
