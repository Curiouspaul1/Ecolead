import os


class Config:
    BASE_URL = os.path.abspath(os.getcwd())
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('app-secret')


class DevConfig(Config):
    DEBUG = True
    ENV = os.getenv('FLASK_ENV')
    SQLALCHEMY_DATABASE_URI = f"sqlite3:///{Config.BASE_URL}/dev.sqlite3"


class ProdConfig(Config):
    DEBUG = False
    ENV = os.getenv('FLASK_ENV')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')


class TestConfig(Config):
    DATABASE_URI = 'sqlite:///:memory:'
    TESTING = True


config_options = {
    "production": ProdConfig,
    "development": DevConfig,
    "testing": TestConfig,
    "default": DevConfig
}
