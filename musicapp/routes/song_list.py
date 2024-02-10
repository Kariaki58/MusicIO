from flask import Flask, redirect, render_template, Blueprint, url_for


song = Blueprint('song', __name__)


@song.route("/api/<playlistid>/songs")
def show_music(playlistid):
    from musicapp.models.song import Song
    
    songs = Song.query.filter(Song.playlist_id==playlistid).all()
    song_content_with_playlist = []
    for song in songs:
        song_content_with_playlist.append(song)
    #may use song_list.html
    return render_template("new_playlist.html", songs=song_content_with_playlist)


# @song.route("/api/<playlistid>/songs/<songid>")
# def show_current_song(playlistid, songid):
#     from musicapp.models.song import Song
#     songs = Song.query.filter(Song.id==songid).all()
#     return render_template("song_list.html", songs=songs)
