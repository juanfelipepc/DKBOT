import threading

from bridge import irc_to_telegram, telegram_to_irc

threads = []

fromtelegram = threading.Thread(target=telegram_to_irc, args=())
fromirc = threading.Thread(target=irc_to_telegram, args=())

fromirc.start()
fromtelegram.start()
