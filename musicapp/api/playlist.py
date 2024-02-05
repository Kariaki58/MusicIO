from flask import jsonify, make_response, request
from musicapp.api import api_views
from musicapp.models.playlist import Playlist



@api_views.route('/playlists', methods=['GET'])
def list_playlists():
    """Returns list of playlists
        
        Args:
          query strings:
            page (int): Page number to return
            page_size (int): number of rows to return in a one page
        Return:
          array of playlists with their songs
    """
    data = []
    page = request.args.get('page', 1)
    page_size = request.args.get('page_size', 1)
    query = Playlist.query
    query.limit(page_size)
    query.offset(page_size * page)
    playlists = query.all()

    for playlist in playlists:
        data_dict = playlist.to_dict()
        del data_dict['_sa_instance_state']
        data.append(data_dict)

    return jsonify(data), 200


@api_views.route('/playlists/<int:playlist_id>/songs', methods=['GET'])
def list_playlist_songs(playlist_id):
    """ Returns songs to playlist"""
    songs = []
    data = Playlist.query.filter_by(id=playlist_id).all()

    for playlist in data:
        songs = playlist.songs
        for song in songs:
            song_dict = song.to_dict()
            songs.append(song)
    return songs, 200
