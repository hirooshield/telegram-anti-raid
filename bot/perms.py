from telegram import ChatPermissions

RaidPermissions = ChatPermissions(can_send_message=False)
NormalPermissions = ChatPermissions(can_send_messages=True)
