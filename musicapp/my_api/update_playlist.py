from . import my_api_views
import secrets
from flask import request, jsonify
from musicapp import database



@my_api_views.route('/update_playlist_name', methods=['POST'])
def update_playlist_name():
    from musicapp.models.playlist import Playlist


    new_playlist_name = request.form.get('playlist_name')

    print(new_playlist_name)
    print("here")
    playlist_change = Playlist.query.filter(Playlist.playlist_name == new_playlist_name).first()
    playlist_change.playlist_name = new_playlist_name

    database.commit()

    return jsonify({'message': 'playlist updated successfully'})
    