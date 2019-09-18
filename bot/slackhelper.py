import time

from slackclient import SlackClient

from config import get_env


class SlackHelper:

    def __init__(self, api_mode=False):
        self.slack_token = get_env('SLACK_API_TOKEN')
        self.slack_client = SlackClient(self.slack_token)
        self.slack_channel = get_env('SLACK_CHANNEL')

        self.bot_name = 'hand_ops'
        self.bot_id = self.slack_client.api_call('auth.test')['user_id']
        print('Bot id: %s' % self.bot_id)
        if self.bot_id is None:
            exit('Error, could not find %s' % self.bot_name)

        print('Api mode: %s' % api_mode)
        if not api_mode:
            self.listen()

    def post_message(self, msg):
        return self.slack_client.api_call(
            'chat.postMessage',
            channel=self.slack_channel,
            text=msg
        )

    def file_upload(self, file_content, file_name, file_type, title=None, ):
        return self.slack_client.api_call(
            'files.upload',
            channels=self.slack_channel,
            content=file_content,
            filename=file_name,
            filetype=file_type,
            initial_comment='{} Log File'.format(file_name),
            title=title
        )

    def user_info(self, uid):
        return self.slack_client.api_call(
            'users.info',
            user=uid,
            token=self.slack_token
        )

    def listen(self):
        if self.slack_client.rtm_connect(with_team_state=False):
            print('Successfully connected, listening for commands')
            while True:
                time.sleep(1)
        else:
            exit('Error, connection failed')
