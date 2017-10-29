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

def general_news(bot, update, section):
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

def discab_news(bot, update):
    """This function is bulit to print Discab general news"""

    general_news(bot, update, 'discab_general')

    return ConversationHandler.END

def biotechnology(bot, update):
    """This function is bulit to print biotechnology news"""

    general_news(bot, update, 'discab_biotechnology')

    return ConversationHandler.END

def medical(bot, update):
    """This function is bulit to print medical news"""

    general_news(bot, update, 'discab_medical')

    return ConversationHandler.END

def motor_science(bot, update):
    """This function is bulit to print motor_science news"""

    general_news(bot, update, 'discab_motor_science')

    return ConversationHandler.END

def psychology(bot, update):
    """This function is bulit to print psychology news"""

    general_news(bot, update, 'discab_psychology')

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

def general_news_on(bot, update, section):
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

def discab_on(bot, update):
    """This function is built to enable discab general news"""

    general_news_on(bot, update, 'discab_general')

    return ConversationHandler.END

def biotechnology_on(bot, update):
    """This function is built to enable biotechnology news"""

    general_news_on(bot, update, 'discab_biotechnology')

    return ConversationHandler.END

def medical_on(bot, update):
    """This function is built to enable medical news"""

    general_news_on(bot, update, 'discab_medical')

    return ConversationHandler.END

def motor_science_on(bot, update):
    """This function is built to enable motor scince news"""

    general_news_on(bot, update, 'discab_motor_science')

    return ConversationHandler.END

def psychology_on(bot, update):
    """This function is built to enable psychology news"""

    general_news_on(bot, update, 'discab_psychology')

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

def general_news_off(bot, update, section):
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

def discab_off(bot, update):
    """This function is built to disable discab general news"""

    general_news_off(bot, update, 'discab_general')

    return ConversationHandler.END

def biotechnology_off(bot, update):
    """This function is built to disable biotechnology news"""

    general_news_off(bot, update, 'discab_biotechnology')

    return ConversationHandler.END

def medical_off(bot, update):
    """This function is built to disable medical news"""

    general_news_off(bot, update, 'discab_medical')

    return ConversationHandler.END

def motor_science_off(bot, update):
    """This function is built to disable motor scince news"""

    general_news_off(bot, update, 'discab_motor_science')

    return ConversationHandler.END

def psychology_off(bot, update):
    """This function is built to disable psychology news"""

    general_news_off(bot, update, 'discab_psychology')

    return ConversationHandler.END
