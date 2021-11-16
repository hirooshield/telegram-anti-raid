from telegram.ext import (
    CommandHandler,
    MessageHandler,
    filters
)
from .perms import (
    RaidPermissions,
    NormalPermissions
)
from decouple import config, Csv

admins = config('admins', cast=Csv(int))


def handle_new_member(update, ctx):
    members = update.message.new_chat_members
    bot = update.message.bot
    mode = ctx.chat_data.get('raid')
    if mode:
        for member in members:
            bot.ban_chat_member(
                chat_id=update.effective_chat.id,
                user_id=member.id,
                until_date=2*60*60
            )


def handle_anti_raid(update, ctx):
    if update.effective_user.id not in admins:
        return False
    try:
        mode = ctx.chat_data['raid']
    except KeyError:
        mode = False

    mode = not mode
    ctx.chat_data['raid'] = mode

    if mode:
        update.effective_chat.set_permissions(RaidPermissions)
    else:
        update.effective_chat.set_permissions(NormalPermissions)

    update.message.reply_text(f'Raid mode: {mode}')


def handle_status(update, ctx):
    try:
        mode = ctx.chat_data['raid']
    except KeyError:
        mode = False

    update.message.reply_text(f'Raid mode: {mode}')


toggle_anti_raid = CommandHandler(
    command='toggle_anti_raid',
    callback=handle_anti_raid
)

status_handler = CommandHandler(
    command='raid_status',
    callback=handle_status
)

new_member_handler = MessageHandler(
    filters=filters.Filters.status_update.new_chat_members,
    callback=handle_new_member
)
