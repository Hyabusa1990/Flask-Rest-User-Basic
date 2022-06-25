import os


def get_database_uri():
    uri = os.environ.get('DATABASE_DRIVER')
    uri = uri + '://'
    uri = uri + os.environ.get('DATABASE_USER')
    uri = uri + ':'
    uri = uri + os.environ.get('DATABASE_PASSWORD')
    uri = uri + '@'
    uri = uri + os.environ.get('DATABASE_SERVER')
    uri = uri + '/'
    uri = uri + os.environ.get('DATABASE_DATABASE')
    return uri


class Config:
    DEBUG = os.environ.get('DEBUG') or True
    SQLALCHEMY_DATABASE_URI = get_database_uri()
    SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS') or False
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'VERY-SECRET-KEY-123'
    JWT_ERROR_MESSAGE_KEY = os.environ.get('JWT_ERROR_MESSAGE_KEY') or 'message'
