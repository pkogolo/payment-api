import os


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = os.getenv('SECRET_KEY')


class DevelopmentConfig(Config):
    DEBUG = True
    TESTING = False
    CSRF_ENABLED = True


app_configuration = {
    'prod': Config,
    'development': DevelopmentConfig
}
