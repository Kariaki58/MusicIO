from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from musicapp.routes.home import home
from flask_cors import CORS
from flask_mail import Mail


database = SQLAlchemy()
login_manager = LoginManager()
mail = Mail()

def create_app():
    """
    TODO the key will be changed soon.
    in app.config['SQLALCHEMY_DATABASE_URI'] = mysql://user@localhost/dbname
    the dbname should be named app
    :return: app
    """
    app = Flask(__name__)
    CORS(app)
    app.config.from_object('musicapp.settings')
    # app.config['UPLOAD_FOLDER'] = 'uploads'
    # app.config['ALLOWED_EXTENSIONS'] = {'mp3', 'wav', 'ogg'}

    from musicapp.models.like import Like
    from musicapp.models.song import Song
    from musicapp.models.user import User
    from musicapp.models.comment import Comment
    from musicapp.models.favourite import Favourite
    from musicapp.models.base_model import BaseModel
    from musicapp.models.playlist import Playlist

    database.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)


    app.register_blueprint(home)

    with app.app_context():
        database.create_all()
    return app
