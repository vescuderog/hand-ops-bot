from flask_api import FlaskAPI

from bot.slackhelper import SlackHelper
from config import get_env, str_to_bool
from config.env import app_env


def create_bot(config_name):
    print('Create bot with config: %s' % config_name)
    app = FlaskAPI(__name__, instance_relative_config=False)
    app.config.from_object(app_env[config_name])
    app.config.from_pyfile('../config/env.py')
    slack_helper = SlackHelper(str_to_bool(get_env('API_MODE')))

    @app.route("/", methods=["GET"])
    def home():
        slack_helper.post_message('Hello Slack! :tada:')

        # Rendering text
        return 'Hello! I am HandOps!'

    return app
