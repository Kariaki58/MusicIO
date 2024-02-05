from flask import Blueprint


api_views = Blueprint('api_views', __name__, url_prefix='/api')

if api_views:
    from musicapp.api.playlist import *
