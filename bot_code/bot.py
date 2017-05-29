# -*- coding: utf-8 -*-

import collections
import logging
import os
import random
import string
from ast import literal_eval
from time import sleep
import configparser
from telegram import ChatAction
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram.parsemode import ParseMode

from bot_code.state_tracker import StateTracker, StoriesHandler

CONFPATH = "config.ini"
conf = configparser.ConfigParser()
if not os.path.exists(CONFPATH):
    print("Creating stub config...\n"
          "You need to replace STUB with your actual token")
    conf["bot"] = {"TOKEN": "STUB", "CONTEXT_SIZE": 3, "REPLY_HIST_SIZE": 20, "LOGFILE": 'log.txt'}
    with open(CONFPATH, 'wt') as configfile:
        conf.write(configfile)

conf.read(CONFPATH)

TOKEN = conf["bot"]["TOKEN"]
CONTEXT_SIZE = conf["bot"]["CONTEXT_SIZE"]
REPLY_HIST_SIZE = conf["bot"]["REPLY_HIST_SIZE"]
LOGFILE = conf["bot"]["LOGFILE"]


# Enable logging
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

fh = logging.FileHandler(LOGFILE)
fh.setLevel(logging.DEBUG)
fh.setFormatter(formatter)

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(formatter)

logger.addHandler(fh)
logger.addHandler(ch)


# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.

class Bot:
    def __init__(self):
        self.history = {}

        self.updater = Updater(TOKEN)
        self.name = str(self).split(' ')[-1][:-1]

        self.dp = self.updater.dispatcher

        self.dp.add_handler(CommandHandler("start", start))
        self.dp.add_handler(CommandHandler("help", help))

        self.dp.add_handler(MessageHandler([Filters.text], echo))

        self.dp.add_error_handler(error)
        self.stories = StoriesHandler()
        logger.info('I\'m alive!')

    def power_on(self):
        # Start the Bot
        self.updater.start_polling()

        # Run the bot until the you press Ctrl-C or the process receives SIGINT,
        # SIGTERM or SIGABRT. This should be used most of the time, since
        # start_polling() is non-blocking and will stop the bot gracefully.
        self.updater.idle()


def mess2dict(mes):
    return literal_eval(str(mes))


def start(bot, update):
    md = mess2dict(update.message)
    sender_id = str(md['from']['id'])
    ai.history[sender_id] = {"state_tracker": StateTracker(ai.stories.get_one()),
                             'context': collections.deque(maxlen=CONTEXT_SIZE),
                             'replies': collections.deque(maxlen=REPLY_HIST_SIZE)}
    if random.random() > 0.5:
        # we decide to go first
        bot_send_message(bot, update, ai.history[sender_id]["state_tracker"].get_question())


def help(bot, update):
    md = mess2dict(update.message)
    sender_id = md['from']['id']
    try:
        sender_fname = md['from']['first_name'].encode('utf-8')
        sender_lname = md['from']['last_name'].encode('utf-8')
    except:
        sender_fname = sender_id
        sender_lname = ''
    help_msg = ("Hello, {} {}!\n\n My name is {}. We can discuss news, "
                "say '/start' to randomly choose a news article.")\
        .format(sender_fname, sender_lname, ai.name)
    bot.sendMessage(update.message.chat_id, text=help_msg, parse_mode=ParseMode.MARKDOWN)


def echo(bot, update):
    text = update.message.text
    md = mess2dict(update.message)
    try:
        sender_fname = md['from']['first_name'].encode('utf-8')
        sender_lname = md['from']['last_name'].encode('utf-8')
    except:
        sender_fname = str(md['from']['id'])
        sender_lname = ""
    logger.info("{} {} says: {}".format(sender_fname, sender_lname, text))

    sender_id = str(md['from']['id'])
    msg_id = str(md["message_id"])

    if text:
        ai.history[sender_id]['context'].append(text)

        rep = ai.history[sender_id]["state_tracker"].get_reply(text)
        ai.history[sender_id]['replies'].append(rep)
        logger.info('Hermes replies: {}'.format(rep))
        bot_send_message(bot, update, rep)


def bot_send_message(bot, update, text):
    bot.sendChatAction(update.message.chat_id, action=ChatAction.TYPING)
    sleep(random.random() * 2 + 1.)
    bot.sendMessage(update.message.chat_id, text=text)


def error(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))


def remove_punktuation(s):
    return ''.join([ch for ch in s if ch not in exclude])


exclude = set(string.punctuation)

if __name__ == "__main__":
    ai = Bot()
    ai.power_on()
