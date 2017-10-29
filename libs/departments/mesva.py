#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The Package that contains all the news commands for the univaq department"""

import telegram
from telegram.ext import ConversationHandler
from libs import utils

def mesva(bot, update):
    """Defining the command to retrieve 5 news"""

    keys = [['In Evidenza'], ['Area Medicina'], ['Area Scienze Ambientali'],
            ['Area Scienze Biologiche'], ['Chiudi']]

    bot.sendMessage(update.message.chat_id,
                    'Scegli la sezione:',
                    reply_markup=telegram.ReplyKeyboardMarkup(
                        keys, one_time_keyboard=True))

    return "mesva"

def general_news(bot, update, section):
    """Defining function that prints 5 news from mesva given section"""

    news_to_string = ""
    for i, item in enumerate(utils.NEWS[section]):
        news_to_string += (str(i + 1) + ' - <a href="{link}">{title}</a>\n\n').format(**item)

    news_to_string += ('<a href="http://mesva.univaq.it/">'
                       'Vedi le altre notizie</a> e attiva le notifiche con /newson per '
                       'restare sempre aggiornato')

    bot.sendMessage(update.message.chat_id,
                    parse_mode='HTML', disable_web_page_preview=True, text=news_to_string,
                    reply_markup=telegram.ReplyKeyboardRemove())

def mesva_news(bot, update):
    """This function is bulit to print mesva general news"""

    general_news(bot, update, 'mesva_general')

    return ConversationHandler.END

def medical(bot, update):
    """This function is bulit to print medical news"""

    general_news(bot, update, 'mesva_medical')

    return ConversationHandler.END

def environmental_science(bot, update):
    """This function is bulit to print biotechnology news"""

    general_news(bot, update, 'mesva_environmental_science')

    return ConversationHandler.END

def biological_science(bot, update):
    """This function is bulit to print medical news"""

    general_news(bot, update, 'mesva_biological_science')

    return ConversationHandler.END

def motor_science(bot, update):
    """This function is bulit to print motor_science news"""

    general_news(bot, update, 'mesva_motor_science')

    return ConversationHandler.END

def mesvaon(bot, update):
    """Defining the command to retrieve 5 news"""

    keys = [['In Evidenza'], ['Area Medicina'], ['Area Scienze Ambientali'],
            ['Area Scienze Biologiche'], ['Chiudi']]

    bot.sendMessage(update.message.chat_id,
                    'Scegli la sezione',
                    reply_markup=telegram.ReplyKeyboardMarkup(
                        keys, one_time_keyboard=True))

    return "mesva"

def general_news_on(bot, update, section):
    """Defining the command to enable notification for mesva section"""

    if update.message.chat_id not in utils.USERS[section]:
        utils.subscribe_user(update.message.chat_id, section)
        bot.sendMessage(update.message.chat_id,
                        text='Notifiche Abilitate!',
                        reply_markup=telegram.ReplyKeyboardRemove())
    else:
        bot.sendMessage(update.message.chat_id,
                        text='Le notifiche sono già abilitate!',
                        reply_markup=telegram.ReplyKeyboardRemove())

def mesva_on(bot, update):
    """This function is built to enable mesva general news"""

    general_news_on(bot, update, 'mesva_general')

    return ConversationHandler.END

def medical_on(bot, update):
    """This function is built to enable medical news"""

    general_news_on(bot, update, 'mesva_medical')

    return ConversationHandler.END

def environmental_science_on(bot, update):
    """This function is built to enable environmental science news"""

    general_news_on(bot, update, 'mesva_environmental_science')

    return ConversationHandler.END

def biological_science_on(bot, update):
    """This function is built to enable biological scince news"""

    general_news_on(bot, update, 'mesva_biological_science')

    return ConversationHandler.END

def mesvaoff(bot, update):
    """Defining the command to retrieve 5 news"""

    keys = [['In Evidenza'], ['Area Medicina'], ['Area Scienze Ambientali'],
            ['Area Scienze Biologiche'], ['Chiudi']]

    bot.sendMessage(update.message.chat_id,
                    'Scegli la sezione',
                    reply_markup=telegram.ReplyKeyboardMarkup(
                        keys, one_time_keyboard=True))

    return "mesva"

def general_news_off(bot, update, section):
    """Defining the command to disable notification for mesva section"""

    if update.message.chat_id in utils.USERS[section]:
        utils.unsubscribe_user(update.message.chat_id, section)
        bot.sendMessage(update.message.chat_id,
                        text='Notifiche Disattivate!',
                        reply_markup=telegram.ReplyKeyboardRemove())
    else:
        bot.sendMessage(update.message.chat_id,
                        text='Per disattivare le notifiche dovresti prima attivarle.',
                        reply_markup=telegram.ReplyKeyboardRemove())

def mesva_off(bot, update):
    """This function is built to disable mesva general news"""

    general_news_off(bot, update, 'mesva_general')

    return ConversationHandler.END

def medical_off(bot, update):
    """This function is built to disable medical news"""

    general_news_off(bot, update, 'mesva_medical')

    return ConversationHandler.END

def environmental_science_off(bot, update):
    """This function is built to disable environmental science news"""

    general_news_off(bot, update, 'mesva_environmental_science')

    return ConversationHandler.END

def biological_science_off(bot, update):
    """This function is built to disable biological scince news"""

    general_news_off(bot, update, 'mesva_biological_science')

    return ConversationHandler.END
