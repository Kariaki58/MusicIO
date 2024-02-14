# from musicapp import database
# from musicapp.models.like import Like
# from flask import jsonify, make_response, request
# from musicapp.api import api_views


# @api_views.route('/like', methods=['POST'])
# def like_a_song():
#     """API endpoint to like a song"""
#     try:
#         validateLikeRequest(request)
#         data = request.json
#         like = Like(user_id=data["user_id"], song_id=data["song_id"])
#         database.session.add(like)
#         database.session.commit()

#         ret = {"error": False, "message" : "song like successful"}
#         return make_response(jsonify(ret), 201)

#     except ValueError as e:
#         # Please log the exception if possible
#         return make_response(jsonify({"error": True, "message" : "Bad request"}), 400)


# def validateLikeRequest(req):
#     """Validate a /like endpoint data"""
#     data = req.json
#     if not data.get("song_id"):
#         raise ValueError("song_id param missing")
#     if not data.get("user_id"):
#         raise ValueError("user_id param missing")
