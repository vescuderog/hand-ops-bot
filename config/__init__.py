from os import path, environ

from dotenv import load_dotenv

env_path = path.join(path.dirname(__file__), path.pardir, '.env')
load_dotenv(env_path, override=True)


def get_env(key):
    return environ.get(key)


def str_to_bool(s):
    if s == 'True':
        return True
    elif s == 'False':
        return False
    else:
        raise ValueError
