import re

import irc
import telegram
from botconfig import sv_address, sv_port, us_pass, us_nick, irc_channel, telegram_group_id, irc_user_dict


GENERAL_MSG_REGEX = re.compile(r':(.*)!.*@.* .* (.*) :(.*)')


def irc_to_telegram():
    irc_message_data = ''
    irc.connect(sv_address, sv_port, us_pass, us_nick)

    while 1:
        irc_message_data = irc.listen(irc_message_data)
        gen_msg = GENERAL_MSG_REGEX.search(str(irc_message_data))

        if gen_msg:
            msg_user, msg_source, msg_text = gen_msg.group(1), gen_msg.group(2), gen_msg.group(3)

            if msg_source == (f'#{irc_channel}'):
                telegram.send_message(telegram_group_id, f'[{msg_user}]: {msg_text}')


def telegram_to_irc():
    prev_telegram_msg = ''

    while 1:
        telegram_message_data = telegram.get_updates()

        if telegram_message_data and (prev_telegram_msg != telegram_message_data):
            try:
                message_source = str(telegram_message_data['result'][0]['message']['chat']['id'])
                message_text = telegram_message_data['result'][0]['message']['text']
                message_user = irc_user_dict[telegram_message_data['result'][0]['message']['from']['username']]

                if message_source == telegram_group_id:
                    irc.message_send('PRIVMSG', f'#{irc_channel} :[{message_user}]: {message_text}')
            except:
                telegram.send_message(telegram_group_id, "That message can\'t be sent through IRC")
            finally:
                prev_telegram_msg = telegram_message_data

