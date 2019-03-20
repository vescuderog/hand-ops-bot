from flask_api import FlaskAPI

from app.slackhelper import SlackHelper
from config.env import app_env


def create_app(config_name):
    app = FlaskAPI(__name__, instance_relative_config=False)
    app.config.from_object(app_env[config_name])
    app.config.from_pyfile('../config/env.py')
    slack_helper = SlackHelper()

    @app.route("/", methods=["GET"])
    def home():
        slack_helper.post_message('Hello Slack! :tada:')

        # rendering text
        return 'Hello HandOps!'

    return app
