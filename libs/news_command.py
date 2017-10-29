#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The Package that contains all the news commands for the univaq department"""

import telegram
from telegram.ext import CommandHandler, ConversationHandler, RegexHandler
from libs.departments import disim, univaq, discab, mesva

def news(bot, update):
    """Defining the command to retrieve 5 news"""

    keys = [['Univaq'], ['Disim'], ['Mesva'],
            ['Discab'], ['Chiudi']]

    bot.sendMessage(update.message.chat_id,
                    'Scegli il dipartimento:',
                    reply_markup=telegram.ReplyKeyboardMarkup(
                        keys, one_time_keyboard=True))

    return "department"

def newson(bot, update):
    """Defining the command to active notifications"""

    keys = [['Univaq'], ['Disim'], ['Mesva'],
            ['Discab'], ['Chiudi']]

    bot.sendMessage(update.message.chat_id,
                    'Scegli il dipartimento:',
                    reply_markup=telegram.ReplyKeyboardMarkup(
                        keys, one_time_keyboard=True))

    return "department"

def newsoff(bot, update):
    """Defining the command to active notifications"""

    keys = [['Univaq'], ['Disim'], ['Mesva'],
            ['Discab'], ['Chiudi']]

    bot.sendMessage(update.message.chat_id,
                    'Scegli il dipartimento:',
                    reply_markup=telegram.ReplyKeyboardMarkup(
                        keys, one_time_keyboard=True))

    return "department"

def close(bot, update):
    """Defining Function for remove keyboard"""

    bot.sendMessage(update.message.chat_id,
                    'Ho chiuso le news!',
                    reply_markup=telegram.ReplyKeyboardRemove())

    return ConversationHandler.END

NEWS_CONV = ConversationHandler(
    entry_points=[CommandHandler('news', news)],
    states={
        "department": [RegexHandler('^(Univaq)$', univaq.univaq),
                       RegexHandler('^(Disim)$', disim.disim),
                       RegexHandler('^(Mesva)$', mesva.mesva),
                       RegexHandler('^(Discab)$', discab.discab),
                      ],
        "univaq": [RegexHandler('^(Ultimissime)$', univaq.ultimissime),
                   RegexHandler('^(In Evidenza)$', univaq.inevidenza)
                  ],
        "mesva": [RegexHandler('^(In Evidenza)$', mesva.mesva_news),
                  RegexHandler('^(Area Medicina)$', mesva.medical),
                  RegexHandler('^(Area Scienze Ambientali)$', mesva.environmental_science),
                  RegexHandler('^(Area Scienze Biologiche)$', mesva.biological_science)
                 ],
        "discab": [RegexHandler('^(News del dipartimento)$', discab.discab_news),
                   RegexHandler('^(Area delle Biotecnologie)$', discab.biotechnology),
                   RegexHandler('^(Area Medica)$', discab.medical),
                   RegexHandler('^(Area delle Scienze Motorie)$', discab.motor_science),
                   RegexHandler('^(Area della Psicologia)$', discab.psychology)
                  ]
    },
    fallbacks=[RegexHandler('^(Chiudi)$', close)]
)

NEWS_ON_CONV = ConversationHandler(
    entry_points=[CommandHandler('newson', newson)],
    states={
        "department": [RegexHandler('^(Univaq)$', univaq.univaqon),
                       RegexHandler('^(Disim)$', disim.disimon),
                       RegexHandler('^(Mesva)$', mesva.mesvaon),
                       RegexHandler('^(Discab)$', discab.discabon),
                      ],
        "mesva": [RegexHandler('^(In Evidenza)$', mesva.mesva_on),
                  RegexHandler('^(Area Medicina)$', mesva.medical_on),
                  RegexHandler('^(Area Scienze Ambientali)$', mesva.environmental_science_on),
                  RegexHandler('^(Area Scienze Biologiche)$', mesva.biological_science_on)
                 ],
        "discab": [RegexHandler('^(News del dipartimento)$', discab.discab_on),
                   RegexHandler('^(Area delle Biotecnologie)$', discab.biotechnology_on),
                   RegexHandler('^(Area Medica)$', discab.medical_on),
                   RegexHandler('^(Area delle Scienze Motorie)$', discab.motor_science_on),
                   RegexHandler('^(Area della Psicologia)$', discab.psychology_on)
                  ]
    },
    fallbacks=[RegexHandler('^(Chiudi)$', close)]
)

NEWS_OFF_CONV = ConversationHandler(
    entry_points=[CommandHandler('newsoff', newsoff)],
    states={
        "department": [RegexHandler('^(Univaq)$', univaq.univaqoff),
                       RegexHandler('^(Disim)$', disim.disimoff),
                       RegexHandler('^(Mesva)$', mesva.mesvaoff),
                       RegexHandler('^(Discab)$', discab.discaboff),
                      ],
        "mesva": [RegexHandler('^(In Evidenza)$', mesva.mesva_off),
                  RegexHandler('^(Area Medicina)$', mesva.medical_off),
                  RegexHandler('^(Area Scienze Ambientali)$', mesva.environmental_science_off),
                  RegexHandler('^(Area Scienze Biologiche)$', mesva.biological_science_off)
                 ],
        "discab": [RegexHandler('^(News del dipartimento)$', discab.discab_off),
                   RegexHandler('^(Area delle Biotecnologie)$', discab.biotechnology_off),
                   RegexHandler('^(Area Medica)$', discab.medical_off),
                   RegexHandler('^(Area delle Scienze Motorie)$', discab.motor_science_off),
                   RegexHandler('^(Area della Psicologia)$', discab.psychology_off)
                  ]
    },
    fallbacks=[RegexHandler('^(Chiudi)$', close)]
)
