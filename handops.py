from bot import create_app, SlackHelper
from config import get_env, str_to_bool

bot = SlackHelper()

if __name__ == '__main__':
    rtm_mode = str_to_bool(get_env('RTM_MODE'))
    print('RTM mode: %s' % rtm_mode)

    if rtm_mode:
        bot.listen()
    else:
        app = create_app(get_env('APP_ENV'), bot)
        app.run()
