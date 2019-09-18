from bot import create_bot
from config import get_env

bot = create_bot(get_env('APP_ENV'))

if __name__ == '__main__':
    print('Running bot...')
    bot.run()
