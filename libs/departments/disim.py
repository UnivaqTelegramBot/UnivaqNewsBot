#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The Package that contains all the news commands for the disim department"""

import telegram
from telegram.ext import ConversationHandler
from libs import utils

def disim(bot, update):
    """Defining the command to retrieve 5 news
    Now we store the last 10 news into the database,
    the comparison to send notifications is made between
    the last 5 pulled news from disim site and the news stored into the db.
    This decision was made to avoid repeated news, in fact, if some news(from first to fifth)
    is deleted the sixth(that now has become the fifth) news will be sent again even if it is
    already been sent in the past because it will appear in the pulled news and it
    is no more present into the database at the moment of the comparison.
    """

    news_to_string = ""
    for i, item in enumerate(utils.NEWS['disim'][0:5]):
        suffix = '...' if len(item['description']) > 75 else ''
        news_to_string += (str(i + 1) + ' - <a href="{link}">{title}</a>\n'
                           '\t<i>{description:.75}{}</i>\n\n').format(suffix, **item)

    news_to_string += ('<a href="http://www.disim.univaq.it/main/news.php?entrant=1">'
                       'Vedi le altre notizie</a> e attiva le notifiche con /newson per '
                       'restare sempre aggiornato')

    bot.sendMessage(update.message.chat_id,
                    parse_mode='HTML', disable_web_page_preview=True, text=news_to_string,
                    reply_markup=telegram.ReplyKeyboardRemove())

    return ConversationHandler.END


def disimon(bot, update):
    """Defining the command to enable notification for disim"""

    if update.message.chat_id not in utils.USERS['disim']:
        utils.subscribe_user(update.message.chat_id, 'disim')
        bot.sendMessage(update.message.chat_id,
                        text='Notifiche Abilitate!')
    else:
        bot.sendMessage(update.message.chat_id,
                        text='Le notifiche sono già abilitate!')

    return ConversationHandler.END


def disimoff(bot, update):
    """Defining the command to disable notification for disim"""

    if update.message.chat_id in utils.USERS['disim']:
        utils.unsubscribe_user(update.message.chat_id, 'disim')
        bot.sendMessage(update.message.chat_id,
                        text='Notifiche Disattivate!')
    else:
        bot.sendMessage(update.message.chat_id,
                        text='Per disattivare le notifiche dovresti prima attivarle.')

    return ConversationHandler.END
