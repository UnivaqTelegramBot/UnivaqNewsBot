#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The Package that contains the conversation handler for user's feedbacks"""

import os
import telegram
from telegram.ext import CommandHandler, ConversationHandler, RegexHandler

def feedback_command(bot, update):
    """Defining the command to ask for user's feedback"""

    keys = [['Lascia un messaggio agli sviluppatori'], ['Chiudi']]

    bot.sendMessage(update.message.chat_id,
                    'Cosa desideri fare?',
                    reply_markup=telegram.ReplyKeyboardMarkup(
                        keys, one_time_keyboard=True))

    return "send_feedback"

def receiving_user_feedback(bot, update):
    """Function to listen for user feedback"""

    bot.sendMessage(update.message.chat_id, 'Scrivi il tuo messaggio:')

    return "message"

def send_to_developers(bot, update):
    """Function to send feedback to developers"""

    feedback_user = (('<b>{}</b>\n\n <i>{} {}, {}</i>')
                     .format(update.message.text,
                             update.message.from_user.first_name,
                             update.message.from_user.last_name,
                             update.message.chat_id))

    for admin in os.environ['ADMIN'].split(' '):
        bot.sendMessage(admin, feedback_user, parse_mode='HTML')

    bot.sendMessage(update.message.chat_id, 'Grazie per la collaborazione, '
                                            'il messaggio è stato inviato agli sviluppatori.',
                    reply_markup=telegram.ReplyKeyboardRemove())

    return ConversationHandler.END

def close(bot, update):
    """Defining Function for remove keyboard"""

    bot.sendMessage(update.message.chat_id,
                    'Davvero non vuoi nemmeno salutarci? Che peccato...',
                    reply_markup=telegram.ReplyKeyboardRemove())

    return ConversationHandler.END

FEEDBACK_CONV = ConversationHandler(
    entry_points=[CommandHandler('feedback', feedback_command)],
    states={
        "send_feedback": [RegexHandler('^(Lascia un messaggio agli sviluppatori)$',
                                       receiving_user_feedback)],
        "message": [RegexHandler('.*', send_to_developers)]
    },
    fallbacks=[RegexHandler('^(Chiudi)$', close)]
)
