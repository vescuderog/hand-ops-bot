__author__ = 'vescudero'

import os


class EnvConfig(object):
    """Parent configuration class"""
    DEBUG = False
    CSRF_ENABLED = True
    SECRET_KEY = os.urandom(16)


class DevelopmentEnv(EnvConfig):
    """Configurations for Development"""
    DEBUG = True


class TestingEnv(EnvConfig):
    """Configurations for Testing, with a separate test database"""
    TESTING = True
    DEBUG = True


class StagingEnv(EnvConfig):
    """Configurations for Staging"""
    DEBUG = True


class ProductionEnv(EnvConfig):
    """Configurations for Production"""
    DEBUG = False
    TESTING = False


app_env = {
    'development': DevelopmentEnv,
    'testing': TestingEnv,
    'staging': StagingEnv,
    'production': ProductionEnv,
}
