__author__ = 'vescudero'

from os import path, environ

from dotenv import load_dotenv

env_path = path.join(path.dirname(__file__), path.pardir, '.env')
load_dotenv(env_path, override=True)


def get_env(key):
    if environ.get(key) is not None:
        return environ.get(key)
    return None


def str_to_bool(string):
    if string:
        if string == 'True':
            return True
    return False
