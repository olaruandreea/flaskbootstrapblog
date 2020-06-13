import os 
'''inspired from https://hackersandslackers.com/configure-flask-applications/'''

class Config:
    """Base config."""
    SECRET_KEY = os.environ.get('SECRET_KEY')
    if not SECRET_KEY:
        raise ValueError("No SECRET_KEY set for Flask application")
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'
    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME =  os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD =  os.environ.get('MAIL_PASSWORD')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevConfig(Config):
    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLITE_URI_DEV')

class TestConfig(Config):
    FLASK_ENV = 'testing'
    DEBUG = False
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLITE_URI_TEST')
    WTF_CSRF_ENABLED = False

