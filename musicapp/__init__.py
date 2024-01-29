from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_cors import CORS
from musicapp.routes.home import home



database = SQLAlchemy()
login_manager = LoginManager()


def create_app():
    """
    TODO the key will be changed soon.
    in app.config['SQLALCHEMY_DATABASE_URI'] = mysql://user:password@localhost/dbname
    the dbname should be named app
    :return: app
    """
    app = Flask(__name__)
    app.config.from_object('musicapp.settings')

    CORS(app)

    database.init_app(app)
    login_manager.init_app(app)

    app.register_blueprint(home)
    
    
    app.app_context().push() #this may work when commented.
    
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    database.create_all()
    return app
