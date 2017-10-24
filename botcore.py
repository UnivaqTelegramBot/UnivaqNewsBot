#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This is the core script of the UnivaqInformaticaBot
created by Giacomo Cerquone e Stefano Martella
"""

import os
from telegram.ext import Updater, CommandHandler

from libs import utils
from libs import news
from libs.departments import disim, univaq, discab, mesva
from libs import other_commands, feedback

def start_command(bot, update):
    """Defining the `start` command"""

    welcome = ("Ciao, sono il bot dell'Univaq (Università dell'Aquila).\n"
               "Posso fornirti tutte le informazioni di cui hai bisogno sulla nostra università, "
               "digita /help per vedere la lista di comandi.")

    utils.add_user(update.message.chat_id)
    bot.sendMessage(update.message.chat_id, text=welcome)


def help_command(bot, update):
    """Defining the `help` command"""

    help_message = ("La lista di comandi:\n\n"
                    "/help - Stampa questo messaggio\n"
                    "/disim - Leggi le ultime 5 news del disim, /disimon o /disimoff"
                    " per abilitare o meno le notifiche\n"
                    "/discab - Leggi le ultime 5 news della sezione che vuoi, /discabon"
                    " o /discaboff per abilitare o meno le notifiche\n"
                    "/mesva - Leggi le ultime 5 news della sezione che vuoi, /mesvaon"
                    " o /mesvaoff per abilitare o meno le notifiche\n"
                    "/prof - Visualizza tutti i docenti\n"
                    "/prof cognome/corso - Info su un docente filtrato per corso o cognome\n"
                    "/segreteria - Info sulla segreteria studenti\n"
                    "/mensa - Info sugli orari della mensa\n"
                    "/adsu - Info sull'adsu\n"
                    "/feedback messaggio - Lascia un messaggio agli sviluppatori"
                    "\n\nQuesto bot è orgogliosamente open source"
                    ", sviluppato e mantenuto da Giacomo Cerquone e Stefano Martella.")

    bot.sendMessage(update.message.chat_id, text=help_message)

def main():
    """Defining the main function"""

    token = os.environ['TELEGRAMBOT'] or os.environ['UNIVERSITYBOT']
    logger = utils.get_logger(os.environ['DEBUG'])
    updater = Updater(token)

    utils.db_connection()
    utils.get_users()
    utils.get_news()

    updater.job_queue.run_repeating(news.notify_news, float(os.environ['NOTIFICATION_INTERVAL']))
    updater.job_queue.run_once(utils.botupdated_message, 0)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start_command))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("disim", disim.disim))
    dispatcher.add_handler(CommandHandler("disimon", disim.disimon))
    dispatcher.add_handler(CommandHandler("disimoff", disim.disimoff))
    dispatcher.add_handler(discab.NEWS_CONV)
    dispatcher.add_handler(discab.NEWS_ON_CONV)
    dispatcher.add_handler(discab.NEWS_OFF_CONV)
    dispatcher.add_handler(mesva.NEWS_CONV)
    dispatcher.add_handler(mesva.NEWS_ON_CONV)
    dispatcher.add_handler(mesva.NEWS_OFF_CONV)
    dispatcher.add_handler(univaq.NEWS_CONV)
    dispatcher.add_handler(CommandHandler("univaqon", univaq.univaqon))
    dispatcher.add_handler(CommandHandler("univaqoff", univaq.univaqoff))
    dispatcher.add_handler(CommandHandler("prof", other_commands.prof_command, pass_args=True))
    dispatcher.add_handler(CommandHandler("segreteria", other_commands.student_office_command))
    dispatcher.add_handler(CommandHandler("mensa", other_commands.canteen_command))
    dispatcher.add_handler(CommandHandler("adsu", other_commands.adsu_command))
    dispatcher.add_handler(feedback.FEEDBACK_CONV)

    logger.info('Bot started')

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
