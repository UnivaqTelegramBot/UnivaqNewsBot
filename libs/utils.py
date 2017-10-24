#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The package that contains groups all the functions needed by other scripts."""

import logging
import os

import bs4
import requests
import pymongo

DATABASE = ""
USERS = {
    'telegramID': [],
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
NEWS = {}


def db_connection():
    """Get MongoDB connection"""

    try:
        conn = pymongo.MongoClient(os.environ['MONGODB_URI'])
        print("Connected successfully!")
    except (pymongo.errors.ConnectionFailure) as err:
        print("Could not connect to MongoDB: %s" % err)

    global DATABASE
    DATABASE = conn.get_default_database()

def get_users():
    """Get from DB all the subscribers"""

    for user in DATABASE.users.find({}, {'_id': False}):
        for section in user:
            USERS[section].append(user[section])

def add_user(telegram_id):
    """Add subscriber to the DB"""

    USERS['telegramID'].append(telegram_id)
    DATABASE.users.insert({"telegramID": telegram_id})

def subscribe_user(telegram_id, section):
    """Add subscriber to the DB"""

    USERS[section].append(telegram_id)
    DATABASE.users.update_one({"telegramID": telegram_id}, {"$set": {section: telegram_id}})

def unsubscribe_user(telegram_id, section):
    """Remove subscriber from DB"""

    USERS[section].remove(telegram_id)
    DATABASE.users.update_one({"telegramID": telegram_id}, {"$unset": {section: ""}})

def get_news():
    """Get all the news"""

    global NEWS
    NEWS = DATABASE['news'].find_one({}, {'_id': False})

def store_news(data):
    # TODO do we need store_news(data, section)?
    """Store all the news"""

    DATABASE['news'].remove({})
    DATABASE['news'].insert(data)

def botupdated_message(bot, job):
    """
    Defining a command to notify the user and tell them what updates have been released
    It is called at every execution ONLY if there are documents in a specific db collection
    """

    messages = list(DATABASE.messages.find())
    DATABASE.messages.remove()

    for message in messages:
        for user in USERS['telegramID']:
            bot.sendMessage(user, message['text'], parse_mode='HTML')

def get_soup_from_url(url):
    """Download a webpage and return its BeautifulSoup"""

    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5)',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'accept-charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'accept-encoding': 'gzip,deflate,sdch',
        'accept-language': 'it-IT',
    }
    request = requests.get(url, headers=headers)
    if request.status_code == 200:
        return bs4.BeautifulSoup(request.text, 'html.parser')

    fmt = 'Error! get_soup_from_url({}) --> Status: {}'
    print(fmt.format(url, request.status_code))
    return None

def get_logger(debug):
    """Get logger object"""

    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO
    )
    logger = logging.getLogger(__name__)

    if debug is False:
        logging.disable(logging.CRITICAL)

    return logger
