__author__ = 'vescudero'

import sys
import time

from bot import event, SlackHelper
from config import get_env


class Bot:

    def __init__(self):
        self.slack_helper = SlackHelper()
        # Get the bot name
        self.bot_name = get_env('BOT_NAME')
        print('Bot name: %s' % self.bot_name)
        # Get the bot id
        self.bot_id = self.slack_helper.get_bot_id()
        if self.bot_id is None:
            sys.exit('Error, could not find %s' % self.bot_name)
        else:
            print('Bot id: %s' % self.bot_id)
        # Init the event class
        self.event = event.Event(self)

    def listen(self):
        if self.slack_helper.slack_client.rtm_connect(with_team_state=False):
            print('Successfully connected, listening for commands')
            while True:
                self.event.wait_for_event()

                time.sleep(1)
        else:
            sys.exit('Error, connection failed')
