#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The Package that contains the conversation handler for user's feedbacks"""

import telegram
from telegram.ext import CommandHandler, ConversationHandler, RegexHandler

def feedback_command(bot, update):
    """Defining the command to ask for user's feedback"""

    keys = [['Lascia un consiglio per gli sviluppatori'], ['Chiudi']]

    bot.sendMessage(update.message.chat_id,
                    'Cosa desideri fare?',
                    reply_markup=telegram.ReplyKeyboardMarkup(
                        keys, one_time_keyboard=True))

    return "option"

def receiving_user_feedback(bot, update):
    """Function to listen for user feedback"""

    bot.sendMessage(update.message.chat_id, 'Scrivi il commento per gli sviluppatori!')

    return "feedback"


def send_to_developers(bot, update):
    """Function to send feedback to developers"""

    feedback_user = (('<b>' + update.message.text + '</b>\n\n <i>{} {}, {}</i>')
                     .format(update.message.from_user.first_name,
                             update.message.from_user.last_name,
                             update.message.chat_id))

    bot.sendMessage(176765549, feedback_user, parse_mode='HTML')
    bot.sendMessage(180852051, feedback_user, parse_mode='HTML')
    bot.sendMessage(update.message.chat_id, 'Grazie per la tua collaborazione,'
                                            'il messaggio è stato inviato agli sviluppatori!',
                    reply_markup=telegram.ReplyKeyboardRemove())

    return ConversationHandler.END

def close(bot, update):
    """Defining Function for remove keyboard"""

    bot.sendMessage(update.message.chat_id,
                    'Ho chiuso il comando per i feedbacks!',
                    reply_markup=telegram.ReplyKeyboardRemove())

    return ConversationHandler.END

FEEDBACK_CONV = ConversationHandler(
    entry_points=[CommandHandler('feedback', feedback_command)],
    states={
        "option": [RegexHandler('^(Lascia un consiglio per gli sviluppatori)$',
                                receiving_user_feedback)],
        "feedback": [RegexHandler('.*', send_to_developers)]
    },
    fallbacks=[RegexHandler('^(Chiudi)$', close)]
)
