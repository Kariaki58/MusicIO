from flask import Flask, redirect, render_template, Blueprint, url_for, jsonify
from flask_login import current_user


song = Blueprint('song', __name__) 


@song.route("/api/<playlistid>/songs")
def show_music(playlistid):
    from musicapp.models.song import Song
    curr_user = None
    if current_user.is_authenticated:
        curr_user = current_user.id
    songs = Song.query.filter(Song.playlist_id==playlistid).all()
    song_content_with_playlist = []
    for song in songs:
        song_dict = song.to_dict()
        song_dict.pop('_sa_instance_state')
        song_content_with_playlist.append(song_dict)
    print(song_content_with_playlist)
    return render_template("new_playlist.html", songs=song_content_with_playlist, curr_user=curr_user)
