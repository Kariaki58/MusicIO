from . import my_api_views
import secrets
from flask import request, jsonify
from musicapp import database


@my_api_views.route('/update_playlist_name', methods=['POST'])
def update_playlist_name():
    from musicapp.models.playlist import Playlist


    new_playlist_name = request.form.get('playlist_name')
    current_user = request.form.get('current_user')

    playlist_change = Playlist.query.filter(Playlist.user_id == current_user).first()

    if not playlist_change:
        return jsonify({'message': 'no playlist created'})
    playlist_change.playlist_name = new_playlist_name

    database.session.commit()

    return jsonify({'message': 'playlist updated successfully'})
