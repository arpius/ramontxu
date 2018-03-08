#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import socket

from requests import get
from telegram.ext import CommandHandler, Filters, MessageHandler, Updater


def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id,
                     text='Hi! I am Ramontxu, can I help you?')


def echo(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=update.message.text)


def greeting(bot, update):
    update.message.reply_text('Hi {}!'.format(
        update.message.from_user.first_name))


def ping(bot, update):
    update.message.reply_text('...pong')


def location(bot, update):
    hostname = socket.gethostname().title()
    public_ip = get('https://icanhazip.com/').text.strip()
    geodata = json.loads(
        get('https://freegeoip.net/json/{}'.format(public_ip)).text)

    update.message.reply_text(
        'I live here! {} [{}, {}]'.format(
            hostname,
            geodata['latitude'],
            geodata['longitude']))


def main():
    updater = Updater('YOUR-TOKEN')
    dispatcher = updater.dispatcher

    start_handler = CommandHandler('start', start)
    greeting_handler = CommandHandler('greeting', greeting)
    ping_handler = CommandHandler('ping', ping)
    location_handler = CommandHandler('location', location)

    echo_handler = MessageHandler(Filters.text, echo)

    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(echo_handler)
    dispatcher.add_handler(greeting_handler)
    dispatcher.add_handler(ping_handler)
    dispatcher.add_handler(location_handler)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
