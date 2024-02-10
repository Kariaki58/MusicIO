from flask import jsonify, make_response, request
from musicapp.api import api_views
from musicapp import database
from musicapp.models.song import Song
from sqlalchemy.orm.exc import NoResultFound


@api_views.route('/songs/<int:id>', methods=['DELETE'])
def remove_song(id):
    """Remove a song

        Request:
          json object: {"song_id": int}

        Response:
          json object: 
              success: {"success": True, "message" : <message>}
              error:   {"error": <error_message>}

    """
    if not id:
        return make_response(jsonify({"error": True, "message" : "Bad request"}), 400)
    try:

        song = Song.query.filter_by(id=id).one()
        database.session.delete(song)
        database.session.commit()

        ret = {"success": True, "message": "song deleted successfully"}
        return make_response(jsonify(ret), 200)
    except NoResultFound as e:
        ret_err = {"error" : True, "message" : "Bad request"}
        return make_response(jsonify(ret_err), 400)
