from bot import create_app, SlackHelper
from config import get_env, str_to_bool

bot = create_app(get_env('APP_ENV'))

if __name__ == '__main__':
    rtm_mode = str_to_bool(get_env('RTM_MODE'))
    print('RTM mode: %s' % rtm_mode)

    if rtm_mode:
        slack_client = SlackHelper()
        slack_client.listen()
    else:
        bot.run()
