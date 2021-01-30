import os


class Config(object):
    DEBUG = False
    TESTING = False
    DATABASE_URI = os.getenv('DATABASE_URI')
    MAX_BOOKS_PER_SALE = os.getenv('MAX_BOOKS_PER_SALE')


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True


def get_configuration_class():
    FLASK_ENV = os.getenv('FLASK_ENV')

    if FLASK_ENV == 'DEVELOPMENT':
        return DevelopmentConfig
    elif FLASK_ENV == 'PRODUCTION':
        return ProductionConfig
    elif FLASK_ENV == 'TESTING':
        return TestingConfig
