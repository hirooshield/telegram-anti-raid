from telegram.ext import (Updater,
                          PicklePersistence)
from dotenv import load_dotenv
from .handler import (
    new_member_handler,
    status_handler,
    toggle_anti_raid
)
import os

load_dotenv()
bot_token = os.getenv('bot_token')

persistence = PicklePersistence(filename='anti_raid_bot.p')
updater = Updater(token=bot_token, persistence=persistence)
dispatcher = updater.dispatcher
dispatcher.add_handler(new_member_handler, group=0)
dispatcher.add_handler(status_handler)
dispatcher.add_handler(toggle_anti_raid)
updater.start_polling()
updater.idle()
