import os

# Application settings
DEBUG = True
APP_NAME = "MusicIO"
APP_SYSTEM_ERROR_SUBJECT_LINE = APP_NAME + " system error"

# Flask settings
FLASK_CSRF_ENABLED = True
SECRET_KEY = 'forsecretkey'

# Flask-SQLAlchemy settings
SQLALCHEMY_DATABASE_URI = 'mysql://root@localhost/musicappdb'
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Flask-User settings
USER_APP_NAME = APP_NAME
USER_AFTER_LOGIN_ENDPOINT = 'main.dashboard'
USER_AFTER_LOGOUT_ENDPOINT = 'main.login'
