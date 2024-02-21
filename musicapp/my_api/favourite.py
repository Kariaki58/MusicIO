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
        favourite = Favourite(user_id=current_user, song_id=song_id, artist_name=song_title, song_path=song.song_path)
        database.session.add(favourite)
        database.session.commit()
    return jsonify({"starred": int(current_user) in map(lambda x: x.user_id, song.favourites)})


@my_api_views.route('/favourite', methods=['POST'])
def get_from_favourite():
    from musicapp.models.favourite import Favourite
    from musicapp.models.song import Song
    from musicapp.models.like import Like


    current_user = request.form.get('user')

    favourites = Favourite.query.filter(Favourite.user_id == current_user).all()
    favourite = [fav.song_id for fav in Favourite.query.filter(Favourite.user_id == current_user).all()]
    liked_songs = [like.song_id for like in Like.query.filter(Like.user_id == current_user).all()]


    fav_list = []

    for fav in favourites:
        json_dict = fav.to_dict()
        json_dict.pop('_sa_instance_state', None)
        json_dict["fav"] = 'fa-solid' if fav.song_id in favourite else 'fa-regular'
        json_dict['liked'] = 'fa-solid' if fav.song_id in liked_songs else 'fa-regular'

        fav_list.append(json_dict)
    return jsonify(fav_list)
