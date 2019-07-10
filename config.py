import os

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = '1234567890'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'wilsenock220@gmail.com'
    MAIL_PASSWORD = '126yzr10382'
    UPLOADED_PHOTOS_DEST ='app/static/photos'

class ProdConfig(Config):
    pass

class TestConfig(Config):
    pass

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:wilstan@localhost/blog'
    DEBUG = True

config_options ={"production":ProdConfig,"default":DevConfig,"testing":TestConfig}

