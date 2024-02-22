from flask import Blueprint


my_api_views = Blueprint('my_api_views', __name__)

if my_api_views:
    from musicapp.my_api.get_playlist import *
    from musicapp.my_api.authentication import *
    from musicapp.my_api.song_list import *
    from musicapp.my_api.remove_song import *
    from musicapp.my_api.like import *
    from musicapp.my_api.favourite import *
    from musicapp.my_api.update_playlist import *
    from musicapp.my_api.del_playlist import *
    from musicapp.my_api.del_account import *
