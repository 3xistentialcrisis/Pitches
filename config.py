import os

class Config:
    """
    General config class
    """

    SECRET_KEY = 'wanjiku'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://ciku:1234@localhost/pitches'
    UPLOADED_PHOTOS_DEST = 'app/static/photos'


class ProdConfig(Config):
    """
    Production configuration child class
    """
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


class DevConfig(Config):
    """
    Development configuration child class
    """


    DEBUG = True

config_options = {
    'development': DevConfig,
    'production': ProdConfig
}
