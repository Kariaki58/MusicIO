from flask import Flask, Blueprint, render_template, jsonify


home = Blueprint("home", __name__)


@home.route('/', methods=['GET'])
def home_page():
    from musicapp.models.song import Song
    content_list = []
    songs = Song.query.all()
    for song in songs:
        song_dict = song.to_dict()
        song_dict.pop('_sa_instance_state', None)
        content_list.append(song_dict)

    return jsonify(content_list)
