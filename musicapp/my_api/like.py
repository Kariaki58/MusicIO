from musicapp import database
from musicapp.models.like import Like
from flask import jsonify, make_response, request
from musicapp.my_api import my_api_views


@my_api_views.route('/like/<int:id>', methods=['POST'])
def like_song(id):
    from musicapp.models.song import Song

    current_user = request.form.get('user')


    song = Song.query.filter_by(id=id).first()
    like = Like.query.filter_by(user_id=current_user, song_id=id).first()

    if not song:
        return jsonify({'error': 'Post don\'t exist'}, 404)
    elif like:
        database.session.delete(like)
        database.session.commit()
    else:
        like = Like(user_id=current_user, song_id=id)
        database.session.add(like)
        database.session.commit()
    return jsonify({'likes': len(song.likes), "liked": int(current_user) in map(lambda x: x.user_id, song.likes)})