import re

import irc
import telegram
from botconfig import sv_address, sv_port, us_pass, us_nick, irc_channel, telegram_group_id

message_data = ''
prev_telegram_msg = ''
GENERAL_MSG_REGEX = re.compile(r':(.*)!.*@.* .* (.*) :(.*)')

irc.connect(sv_address, sv_port, us_pass, us_nick)

while 1:
    message_data = irc.listen(message_data)
    telegram_msg = telegram.get_updates()
    gen_msg = GENERAL_MSG_REGEX.search(str(message_data))

    if gen_msg:
        msg_user, msg_source, msg_text = gen_msg.group(1), gen_msg.group(2), gen_msg.group(3)

        if msg_source == (f'#{irc_channel}'):
            print(msg_text)
            telegram.send_message(telegram_group_id, f'[{msg_user}]: {msg_text}')

    # Temporary telegram message checking for testing purposes
    if telegram_msg and (prev_telegram_msg != telegram_msg):
        prev_telegram_msg = telegram_msg
        print(telegram_msg)
