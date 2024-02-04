from flask import Flask, redirect, render_template, Blueprint, url_for


song = Blueprint('song', __name__)


@song.route("/api/<playlistid>/songs")
def show_music(playlistid):
    from musicapp.models.song import Song
    
    songs = Song.query.filter(Song.playlist_id==playlistid).all()
    song_content_with_playlist = []
    for song in songs:
        song_content_with_playlist.append(song)
    
    return render_template("song_list.html", songs=song_content_with_playlist)
