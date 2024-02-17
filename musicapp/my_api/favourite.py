from . import my_api_views
import secrets
from flask import request, jsonify
from musicapp import database


@my_api_views.route('/favourite/<int:song_id>', methods=['POST'])
def add_to_favourte(song_id):
    from musicapp.models.favourite import Favourite
    from musicapp.models.song import Song

    
    current_user = request.form.get('current_user')
    song_title = request.form.get('song_name')
    
    song = Song.query.filter_by(id=song_id).first()
    favourite = Favourite.query.filter_by(user_id=current_user, song_id=song_id).first()

    if not song:
        return jsonify({'error': 'song don\'t exist'}, 404)
    elif favourite:
        database.session.delete(favourite)
        database.session.commit()
    else:
        favourite = Favourite(user_id=current_user, song_id=song_id, artist_name=song_title)
        database.session.add(favourite)
        database.session.commit()
    print(int(current_user) in map(lambda x: x.user_id, song.favourites))  
    return jsonify({"starred": int(current_user) in map(lambda x: x.user_id, song.favourites)})
