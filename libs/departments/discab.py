#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The Package that contains all the news commands for the univaq department"""

import telegram
from telegram.ext import CommandHandler, ConversationHandler, RegexHandler
from libs import utils

def discab(bot, update):
    """Defining the command to retrieve 5 news"""

    keys = [['Notizie del dipartimento'], ['Biotecnologie'], ['Area Medica'],
            ['Scienze Motorie'], ['Psicologia'], ['Chiudi']]

    bot.sendMessage(update.message.chat_id,
                    'Scegli la sezione',
                    reply_markup=telegram.ReplyKeyboardMarkup(
                        keys, one_time_keyboard=True))

    return "option"

def general_news(bot, update, section):
    """Defining function that prints 5 news from Discab given section"""

    news_to_string = ""
    for i, item in enumerate(utils.NEWS[section][0:5]):
        news_to_string += (str(i + 1) + ' - <a href="{link}">{title}</a>\n\n').format(**item)

    news_to_string += ('<a href="http://discab.univaq.it/index.php?id=2004">'
                       'Vedi le altre notizie</a> e attiva le notifiche con /discabon per '
                       'restare sempre aggiornato')

    bot.sendMessage(update.message.chat_id,
                    parse_mode='HTML', disable_web_page_preview=True, text=news_to_string,
                    reply_markup=telegram.ReplyKeyboardRemove())

def discab_news(bot, update):
    """This function is bulit to print Discab general news"""

    general_news(bot, update, 'general_discab')

    return ConversationHandler.END

def biotechnology(bot, update):
    """This function is bulit to print biotechnology news"""

    general_news(bot, update, 'biotechnology')

    return ConversationHandler.END

def medical(bot, update):
    """This function is bulit to print medical news"""

    general_news(bot, update, 'medical')

    return ConversationHandler.END

def motor_science(bot, update):
    """This function is bulit to print motor_science news"""

    general_news(bot, update, 'motor_science')

    return ConversationHandler.END

def psychology(bot, update):
    """This function is bulit to print psychology news"""

    general_news(bot, update, 'psychology')

    return ConversationHandler.END

def discabon(bot, update):
    """Defining the command to retrieve 5 news"""

    keys = [['Notizie del dipartimento'], ['Biotecnologie'], ['Area Medica'],
            ['Scienze Motorie'], ['Psicologia'], ['Chiudi']]

    bot.sendMessage(update.message.chat_id,
                    'Scegli la sezione',
                    reply_markup=telegram.ReplyKeyboardMarkup(
                        keys, one_time_keyboard=True))

    return "option"

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

    general_news_on(bot, update, 'general_discab')

    return ConversationHandler.END

def biotechnology_on(bot, update):
    """This function is built to enable biotechnology news"""

    general_news_on(bot, update, 'biotechnology')

    return ConversationHandler.END

def medical_on(bot, update):
    """This function is built to enable medical news"""

    general_news_on(bot, update, 'medical')

    return ConversationHandler.END

def motor_science_on(bot, update):
    """This function is built to enable motor scince news"""

    general_news_on(bot, update, 'motor_science')

    return ConversationHandler.END

def psychology_on(bot, update):
    """This function is built to enable psychology news"""

    general_news_on(bot, update, 'psychology')

    return ConversationHandler.END

def discaboff(bot, update):
    """Defining the command to retrieve 5 news"""

    keys = [['Notizie del dipartimento'], ['Biotecnologie'], ['Area Medica'],
            ['Scienze Motorie'], ['Psicologia'], ['Chiudi']]

    bot.sendMessage(update.message.chat_id,
                    'Scegli la sezione',
                    reply_markup=telegram.ReplyKeyboardMarkup(
                        keys, one_time_keyboard=True))

    return "option"

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

    general_news_off(bot, update, 'general_discab')

    return ConversationHandler.END

def biotechnology_off(bot, update):
    """This function is built to disable biotechnology news"""

    general_news_off(bot, update, 'biotechnology')

    return ConversationHandler.END

def medical_off(bot, update):
    """This function is built to disable medical news"""

    general_news_off(bot, update, 'medical')

    return ConversationHandler.END

def motor_science_off(bot, update):
    """This function is built to disable motor scince news"""

    general_news_off(bot, update, 'motor_science')

    return ConversationHandler.END

def psychology_off(bot, update):
    """This function is built to disable psychology news"""

    general_news_off(bot, update, 'psychology')

    return ConversationHandler.END

def close(bot, update):
    """Defining Function for remove keyboard"""

    bot.sendMessage(update.message.chat_id,
                    'Ho chiuso le news del Discab!',
                    reply_markup=telegram.ReplyKeyboardRemove())

    return ConversationHandler.END

NEWS_CONV = ConversationHandler(
    entry_points=[CommandHandler('discab', discab)],
    states={
        "option": [RegexHandler('^(Notizie del dipartimento)$', discab_news),
                   RegexHandler('^(Biotecnologie)$', biotechnology),
                   RegexHandler('^(Area Medica)$', medical),
                   RegexHandler('^(Scienze Motorie)$', motor_science),
                   RegexHandler('^(Psicologia)$', psychology)]
    },
    fallbacks=[RegexHandler('^(Chiudi)$', close)]
)

NEWS_ON_CONV = ConversationHandler(
    entry_points=[CommandHandler('discabon', discabon)],
    states={
        "option": [RegexHandler('^(Notizie del dipartimento)$', discab_on),
                   RegexHandler('^(Biotecnologie)$', biotechnology_on),
                   RegexHandler('^(Area Medica)$', medical_on),
                   RegexHandler('^(Scienze Motorie)$', motor_science_on),
                   RegexHandler('^(Psicologia)$', psychology_on)]
    },
    fallbacks=[RegexHandler('^(Chiudi)$', close)]
)

NEWS_OFF_CONV = ConversationHandler(
    entry_points=[CommandHandler('discaboff', discaboff)],
    states={
        "option": [RegexHandler('^(Notizie del dipartimento)$', discab_off),
                   RegexHandler('^(Biotecnologie)$', biotechnology_off),
                   RegexHandler('^(Area Medica)$', medical_off),
                   RegexHandler('^(Scienze Motorie)$', motor_science_off),
                   RegexHandler('^(Psicologia)$', psychology_off)]
    },
    fallbacks=[RegexHandler('^(Chiudi)$', close)]
)
