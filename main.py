import irc
import telegram
from botconfig import sv_address, sv_port, us_pass, us_nick


irc.connect(sv_address, sv_port, us_pass, us_nick)

while 1:
    irc.listen()

# telegram.get_updates()
# telegram.send_message('', '')
