#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Simple Bot to reply to Telegram messages
# This program is dedicated to the public domain under the CC0 license.
"""
This Bot uses the Updater class to handle the bot.
First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.
Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.DEBUG)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
def start(bot, update):
    update.message.reply_text('Hi!')


def help(bot, update):
    update.message.reply_text('Help!')

tasklist = []

def echo(bot, update):
    dict_done_task = {("i"),("all")}

    cmd = (update.message.text.split(" ")[0])
    thing = ''.join(update.message.text.split(" ")[1:])

    if cmd == "add":
        tasklist.append(thing)
        update.message.reply_text(thing)

    elif cmd == "delete":
        tasklist.remove(thing)
        update.message.reply_text(thing)

    elif cmd == "show":
        if tasklist == [] :
            update.message.reply_text("I have nothing for you")
        else :
            for task in tasklist :
                update.message.reply_text(task)

    elif cmd == "done":
        for st in thing :
            str += st
        dict_done_task[str] = update.message.from_user.first_name
        tasklist.remove(thing)

    elif cmd == "w&w":
        update.message.reply_text(dict_done_task)

    else:
        update.message.reply_text("Sorry, I don't get you")


def error(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))


def test(bot, update):
    update.message.reply_text('Test is working!')


def main():
    # Create the EventHandler and pass it your bot's token.
    updater = Updater("463571123:AAGQhdVA_WN94t44RwqQX4VG7dM7J79QGMY")

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("test", test))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()