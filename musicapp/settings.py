import os

# Application settings
DEBUG = True
APP_NAME = "MusicIO"
SERVER_HOST='localhost'
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
TEMPLATES_AUTO_RELOAD=True

PRESERVE_CONTEXT_ON_EXCEPTION = False

UPLOAD_FOLDER = os.path.join('musicapp', 'static', 'uploads')

ALLOWED_EXTENSIONS = {'mp3', 'wav', 'ogg'}
#Email settings
MAIL_SERVER='smtp.gmail.com'
MAIL_PORT=465
MAIL_USERNAME=''
MAIL_PASSWORD=''
MAIL_DEFAULT_SENDER='info@musicio.com'
MAIL_USE_SSL=True
MAIL_USE_TLS=False
RESET_TEMPLATE= '<p>Dear {}</p></br></br> You have requested to reset your password, Please click the  link to reset your password <a href="{}">Reset</a></br></br> <p>if you didn\'t request to reset your password, please ignore this email</p>' 
