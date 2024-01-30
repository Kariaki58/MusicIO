from flask import Blueprint


auth_views = Blueprint('auth_views', __name__,  static_folder='static')

if auth_views:
    from musicapp.authentication.auth import *
