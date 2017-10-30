#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The Package that contains all the news commands for the disim department"""

from libs import utils

def disim(bot, update):
    """Defining the command to retrieve 5 news"""

    news_to_string = ""
    for i, item in enumerate(utils.NEWS['disim'][0:5]):
        suffix = '...' if len(item['description']) > 75 else ''
        news_to_string += (str(i + 1) + ' - <a href="{link}">{title}</a>\n'
                           '\t<i>{description:.75}{}</i>\n\n').format(suffix, **item)

    news_to_string += ('<a href="http://www.disim.univaq.it/main/news.php?entrant=1">'
                       'Vedi le altre notizie</a> e attiva le notifiche con /disimon per '
                       'restare sempre aggiornato')

    bot.sendMessage(update.message.chat_id,
                    parse_mode='HTML', disable_web_page_preview=True, text=news_to_string)


def disimon(bot, update):
    """Defining the command to enable notification for disim"""

    if update.message.chat_id not in utils.USERS['disim']:
        utils.subscribe_user(update.message.chat_id, 'disim')
        bot.sendMessage(update.message.chat_id,
                        text='Notifiche Abilitate!')
    else:
        bot.sendMessage(update.message.chat_id,
                        text='Le notifiche sono già abilitate!')


def disimoff(bot, update):
    """Defining the command to disable notification for disim"""

    if update.message.chat_id in utils.USERS['disim']:
        utils.unsubscribe_user(update.message.chat_id, 'disim')
        bot.sendMessage(update.message.chat_id,
                        text='Notifiche Disattivate!')
    else:
        bot.sendMessage(update.message.chat_id,
                        text='Per disattivare le notifiche dovresti prima attivarle.')
