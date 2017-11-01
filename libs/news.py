#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The Package that contains all the telegram's news functions used"""

from telegram import TelegramError

from libs import utils
from libs.news_scrapers import disim, univaq, discab, mesva

def pull_news():
    """This function is built to pull 5 news from all the websites"""

    scrapers = {
        'disim': disim.scraper,
        'univaq': univaq.scraper,
        'discab_general': discab.general_news,
        'discab_biotechnology': discab.biotechnology_news,
        'discab_medical': discab.medical_news,
        'discab_motor_science': discab.motor_science_news,
        'discab_psychology': discab.psychology_news,
        'mesva_general': mesva.general_news,
        'mesva_medical': mesva.medical_news,
        'mesva_environmental_science': mesva.environmental_science_news,
        'mesva_biological_science': mesva.biological_science_news
    }
    news = {}

    for key in scrapers:
        news[key] = scrapers[key]()

    return news


def check_news():
    """This function checks if there are some unread news from the website"""

    pulled_news = pull_news()
    stored_news = utils.NEWS
    unread_news = {
        'disim': [],
        'univaq': [],
        'discab_general': [],
        'discab_biotechnology': [],
        'discab_medical':[],
        'discab_motor_science': [],
        'discab_psychology': [],
        'mesva_general': [],
        'mesva_medical': [],
        'mesva_environmental_science': [],
        'mesva_biological_science': []
    }

    # TODO _id field coming back don't know why
    for section in stored_news:
        if section != '_id':
            unread_news[section] = ([x for x in pulled_news[section][0:5]
                                     if x not in stored_news[section]])

    return {'unread_news': unread_news,
            'pulled_news': pulled_news}


def notify_news(bot, job):
    """Defining method that will be repeated over and over"""

    translation = {
        'disim': 'Disim',
        'univaq': 'Univaq',
        'discab_general': 'Discab',
        'discab_biotechnology': 'Biotecnologie',
        'discab_medical': 'Discab Medicina',
        'discab_motor_science': 'Scienze Motorie',
        'discab_psychology': 'Psicologia',
        'mesva_general': 'Mesva',
        'mesva_medical': 'Mesva Medicina',
        'mesva_environmental_science': 'Scienze Ambientali',
        'mesva_biological_science': 'Scienze Biologiche'
    }

    checked = check_news()
    unread_news = checked['unread_news']
    pulled_news = checked['pulled_news']
    invalid_chatid = []

    for section in unread_news:
        if unread_news[section]:
            news_to_string = "<b>"+translation[section]+"</b>\n\n"

            utils.NEWS = pulled_news
            utils.store_news(pulled_news)

            for item in unread_news[section]:
                news_to_string += ('- <a href="{link}">{title}</a>\n'
                                   '\t<i>{description}</i>\n\n').format(**item)

            for chat_id in utils.USERS[section]:
                try:
                    bot.sendMessage(chat_id, parse_mode='HTML', disable_web_page_preview=True,
                                    text=news_to_string)
                except TelegramError:
                    invalid_chatid.append(chat_id)

            for chat_id in invalid_chatid:
                utils.USERS[section].remove(chat_id)
                utils.unsubscribe_user(chat_id, section)
