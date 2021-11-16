from telegram.ext import (Updater,
                          PicklePersistence)
from decouple import config
from .handler import (
    new_member_handler,
    status_handler,
    toggle_anti_raid
)

bot_token = config('bot_token')

persistence = PicklePersistence(filename='anti_raid_bot.p')
updater = Updater(token=bot_token, persistence=persistence)
dispatcher = updater.dispatcher
dispatcher.add_handler(new_member_handler, group=0)
dispatcher.add_handler(status_handler)
dispatcher.add_handler(toggle_anti_raid)
updater.start_polling()
updater.idle()
