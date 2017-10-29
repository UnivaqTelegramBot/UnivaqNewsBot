#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The Package that contains all the news commands for the univaq department"""

import telegram
from telegram.ext import ConversationHandler
from libs import utils

def univaq(bot, update):
    """Defining the command to retrieve 5 news"""

    keys = [['In Evidenza'], ['Ultimissime'], ['Chiudi']]

    bot.sendMessage(update.message.chat_id,
                    'Scegli la sezione:',
                    reply_markup=telegram.ReplyKeyboardMarkup(
                        keys, one_time_keyboard=True))

    return "univaq"

def inevidenza(bot, update):
    """Defining function that prints 5 news from in evidenza"""

    news_to_string = ""
    for i, item in enumerate(utils.NEWS['univaq'][0:5]):
        news_to_string += (str(i + 1) + ' - <a href="{link}">{title}</a>\n\n').format(**item)

    news_to_string += ('<a href="http://www.univaq.it">'
                       'Vedi le altre notizie</a> e attiva le notifiche con /newson per '
                       'restare sempre aggiornato')

    bot.sendMessage(update.message.chat_id,
                    parse_mode='HTML', disable_web_page_preview=True, text=news_to_string,
                    reply_markup=telegram.ReplyKeyboardRemove())

    return ConversationHandler.END

def ultimissime(bot, update):
    """Defining function that prints 5 news from ultimissime"""

    news_to_string = ""
    for i, item in enumerate(utils.NEWS['univaq'][5:10]):
        news_to_string += (str(i + 1) + ' - <a href="{link}">{title}</a>\n\n').format(**item)

    news_to_string += ('<a href="http://www.univaq.it">'
                       'Vedi le altre notizie</a> e attiva le notifiche con /univaqon per '
                       'restare sempre aggiornato')

    bot.sendMessage(update.message.chat_id,
                    parse_mode='HTML', disable_web_page_preview=True, text=news_to_string,
                    reply_markup=telegram.ReplyKeyboardRemove())

    return ConversationHandler.END

def univaqon(bot, update):
    """Defining the command to enable notification for univaq"""

    if update.message.chat_id not in utils.USERS['univaq']:
        utils.subscribe_user(update.message.chat_id, 'univaq')
        bot.sendMessage(update.message.chat_id,
                        text='Notifiche Abilitate!')
    else:
        bot.sendMessage(update.message.chat_id,
                        text='Le notifiche sono già abilitate!')

    return ConversationHandler.END


def univaqoff(bot, update):
    """Defining the command to disable notification for univaq"""

    if update.message.chat_id in utils.USERS['univaq']:
        utils.unsubscribe_user(update.message.chat_id, 'univaq')
        bot.sendMessage(update.message.chat_id,
                        text='Notifiche Disattivate!',
                        reply_markup=telegram.ReplyKeyboardRemove())

    else:
        bot.sendMessage(update.message.chat_id,
                        text='Per disattivare le notifiche dovresti prima attivarle.',
                        reply_markup=telegram.ReplyKeyboardRemove())

    return ConversationHandler.END
