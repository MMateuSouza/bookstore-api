from os import getenv


class Config(object):
    DEBUG = False
    TESTING = False
    DATABASE_URI = SQLALCHEMY_DATABASE_URI = getenv('DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAX_BOOKS_PER_SALE = getenv('MAX_BOOKS_PER_SALE')


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
