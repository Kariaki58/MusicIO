from flask import jsonify, make_response, request
from flask_login import current_user
from musicapp.my_api import my_api_views
from musicapp import database
from musicapp.models.user import User
from sqlalchemy.orm.exc import NoResultFound


@my_api_views.route('/users/del', methods=['DELETE'])
def remove_song():
    """Remove a user
        Request:
          urlencoded form data: user_id

        Response:
          json object: 
              success: {"success": True, "message" : <message>}
              error:   {"error": <error_message>}
    """
    if not id:
        return make_response(jsonify({"error": True, "message" : "Bad request"}), 400)
    try:
        user_id = request.form.get('current_user')
        user = User.query.filter(User.id == user_id).one()
        if (user):
            database.session.delete(user)
            database.session.commit()
            
            ret = {"success": True, "message": "playlist deleted successfully"}
            return make_response(jsonify(ret), 200)
        else:
            raise NoResultFound("you are not allowed")
    except NoResultFound as e:
        ret_err = {"success" : False, "message" : "Bad request"}
        return make_response(jsonify(ret_err), 400)
