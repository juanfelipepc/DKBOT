import re

import irc
import telegram
from botconfig import sv_address, sv_port, us_pass, us_nick, irc_channel

message_data = ''
GENERAL_MSG_REGEX = re.compile(r':(.*)!.*@.* .* (.*) :(.*)')

irc.connect(sv_address, sv_port, us_pass, us_nick)

while 1:
    message_data = irc.listen(message_data)
    gen_msg = GENERAL_MSG_REGEX.search(str(message_data))

    if gen_msg:
        print("MAIN:")
        print(gen_msg.groups())
        msg_source = gen_msg.group(2)
        msg_text = gen_msg.group(3)

        if msg_source == irc_channel:
            print(msg_text)

# telegram.get_updates()
# telegram.send_message('', '')
