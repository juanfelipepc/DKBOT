import socket
import time
import re

from botconfig import bot_owner, irc_channel


irc_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
BUFFER_SIZE = 2048

CMD_MSG_REGEX = re.compile(r':(.*)!.*@.* .* (.*) :.*: (.*)')


def message_send(prefix: str = "", data: str = ""):
    """Sends a command to IRC through the socket"""

    irc_sock.send(prefix.encode('utf-8') + b' ' + data.encode('utf-8') + b'\r\n')
    print(prefix.encode('utf-8') + b' ' + data.encode('utf-8') + b'\r\n')
    time.sleep(0.01)


def connect(ip, port, password, nick):
    """Connects to IRC through a socket"""
    
    print("Connecting...")
    irc_sock.connect((ip, port))
    # Latency protection
    time.sleep(2)
    print("Connected")

    message_send('PASS', password)
    message_send('NICK', nick)
    message_send('USER', 'DOE 0 * :realname')
    

def listen(coming_data):
    """Reads messages sent directly to the bot, or in any channel it's in"""

    msg_user, msg_source, msg_text = "", "", ""

    if not coming_data:
        raw_data = irc_sock.recv(BUFFER_SIZE).decode("utf-8")
        return raw_data
    else:
        formatted_data = coming_data.split('\r\n')

        for sentence in formatted_data:
            cmd_msg = CMD_MSG_REGEX.search(sentence)
            if cmd_msg:
                msg_user = cmd_msg.group(1)
                msg_source = cmd_msg.group(2)
                msg_text = cmd_msg.group(3)
                print(cmd_msg.groups())
            print(sentence)

            if 'PING :' in sentence:
                # Necessary response message to keep alive the connection
                ping_echo = sentence[6:]
                print('PONG :' + ping_echo)
                message_send('PONG', ping_echo)
                return
            elif (":DKBOT:" in sentence) and (msg_user == bot_owner):
                run_command(cmd_msg)
                return
            elif irc_channel == msg_source:
                return msg_user, msg_source, msg_text


def run_command(priv_msg_data):
    """Runs a command from any prefix given, as long as it's sent through IRC by
        the bot owner and following the PRIVMSG DKBOT: <command> <arguments> syntax
        For more information on IRC commands:
        https://en.wikipedia.org/wiki/List_of_Internet_Relay_Chat_commands"""

    data = priv_msg_data.group(3)

    try:
        split_data = data.split(' ', 1)
        bot_command, message = split_data
    except ValueError:
        print("Invalid command syntax")
        return

    message_send(bot_command, message)
