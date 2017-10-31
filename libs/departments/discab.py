#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The Package that contains all the news commands for the univaq department"""

import telegram
from telegram.ext import ConversationHandler
from libs import utils

def discab(bot, update):
    """Defining the command to retrieve 5 news"""

    keys = [['News del dipartimento'], ['Area delle Biotecnologie'], ['Area Medica'],
            ['Area delle Scienze Motorie'], ['Area della Psicologia'], ['Chiudi']]

    bot.sendMessage(update.message.chat_id,
                    'Scegli la sezione',
                    reply_markup=telegram.ReplyKeyboardMarkup(
                        keys, one_time_keyboard=True))

    return "discab"

def discab_news(bot, update, section):
    """Defining function that prints 5 news from Discab given section"""

    news_to_string = ""
    for i, item in enumerate(utils.NEWS[section]):
        news_to_string += (str(i + 1) + ' - <a href="{link}">{title}</a>\n\n').format(**item)

    news_to_string += ('<a href="http://discab.univaq.it/index.php?id=2004">'
                       'Vedi le altre notizie</a> e attiva le notifiche con /newson per '
                       'restare sempre aggiornato')

    bot.sendMessage(update.message.chat_id,
                    parse_mode='HTML', disable_web_page_preview=True, text=news_to_string,
                    reply_markup=telegram.ReplyKeyboardRemove())

    return ConversationHandler.END

def discabon(bot, update):
    """Defining the command to retrieve 5 news"""

    keys = [['News del dipartimento'], ['Area delle Biotecnologie'], ['Area Medica'],
            ['Area delle Scienze Motorie'], ['Area della Psicologia'], ['Chiudi']]

    bot.sendMessage(update.message.chat_id,
                    'Scegli la sezione',
                    reply_markup=telegram.ReplyKeyboardMarkup(
                        keys, one_time_keyboard=True))

    return "discab"

def discab_news_on(bot, update, section):
    """Defining the command to enable notification for discab section"""

    if update.message.chat_id not in utils.USERS[section]:
        utils.subscribe_user(update.message.chat_id, section)
        bot.sendMessage(update.message.chat_id,
                        text='Notifiche Abilitate!',
                        reply_markup=telegram.ReplyKeyboardRemove())
    else:
        bot.sendMessage(update.message.chat_id,
                        text='Le notifiche sono già abilitate!',
                        reply_markup=telegram.ReplyKeyboardRemove())

    return ConversationHandler.END

def discaboff(bot, update):
    """Defining the command to retrieve 5 news"""

    keys = [['News del dipartimento'], ['Area delle Biotecnologie'], ['Area Medica'],
            ['Area delle Scienze Motorie'], ['Area della Psicologia'], ['Chiudi']]

    bot.sendMessage(update.message.chat_id,
                    'Scegli la sezione',
                    reply_markup=telegram.ReplyKeyboardMarkup(
                        keys, one_time_keyboard=True))

    return "discab"

def discab_news_off(bot, update, section):
    """Defining the command to disable notification for discab section"""

    if update.message.chat_id in utils.USERS[section]:
        utils.unsubscribe_user(update.message.chat_id, section)
        bot.sendMessage(update.message.chat_id,
                        text='Notifiche Disattivate!',
                        reply_markup=telegram.ReplyKeyboardRemove())
    else:
        bot.sendMessage(update.message.chat_id,
                        text='Per disattivare le notifiche dovresti prima attivarle.',
                        reply_markup=telegram.ReplyKeyboardRemove())

    return ConversationHandler.END
