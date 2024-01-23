from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


database = SQLAlchemy()
login_manager = LoginManager()


def create_app():
    """
    TODO the key will be changed soon.
    in app.config['SQLALCHEMY_DATABASE_URI'] = mysql://user@localhost/dbname
    the dbname should be named app
    :return: app
    """
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'forsecretkey'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/musicappdb'

    from musicapp.models.likedb import Like
    from musicapp.models.songdb import Song
    from musicapp.models.userdb import User
    from musicapp.models.commentdb import Comment
    from musicapp.models.favouritedb import Favourite
    from musicapp.models.dbmodels import BaseModel
    from musicapp.models.playlist import Playlist

    database.init_app(app)
    login_manager.init_app(app)

    app.app_context().push() #this may work when commented.

    database.create_all()

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    return app