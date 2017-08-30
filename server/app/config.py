import logging

class Default(object):
    LOG_LEVEL = logging.INFO
    PROPAGATE_EXCEPTIONS = True
    SQLALCHEMY_POOL_SIZE = 5
    SQLALCHEMY_POOL_TIMEOUT = 10
    SQLALCHEMY_POOL_RECYCLE = 3600
    SQLALCHEMY_MAX_OVERFLOW = 5
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class Development(Default):
    LOG_LEVEL = logging.DEBUG
    SQLALCHEMY_DATABASE_URI = \
        'mysql://todos:todos@192.168.99.100:3306/todos'
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = True

class CI(Default):
    LOG_LEVEL = logging.DEBUG
    SQLALCHEMY_DATABASE_URI = \
        'mysql://root:@127.0.0.1:3306/circle_test'
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = True
