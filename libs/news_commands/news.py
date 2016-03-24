#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The Package that contains all the telegram's news functions used"""

import os
import sys
sys.path.insert(0, '../')
from libs.utils import utils

def news_command(bot, update, args=None):
    """Defining the `news` command"""

    max_articles = min(int(args[0]) if args else 10, 10)
    news_array = utils.read_json("json/news.json")[:max_articles]
    fmt = '{}- [{title}]({link})\n{description:.75}{suffix}\n'
    news_to_string = ""
    for i, item in enumerate(news_array):
        if item['description'].endswith('... ...'):  # if double elipsess
            item['description'] = item['description'][:-7]  # remove them
        item["suffix"] = '...' if len(item['description']) > 75 else ''
        news_to_string += fmt.format(i+1, **item)

    bot.sendMessage(update.message.chat_id, parse_mode='Markdown', text=news_to_string)

def pull_news(num):
    """This function is built to pull 10 (or an arbitrary number) news from the news page"""

    # Thanks to Luca Pattavina for giving me the right url
    if num <= 5:
        news_urls = ("http://www.disim.univaq.it/main/news.php?entrant=1")
    else:
        news_urls = ("http://www.disim.univaq.it/main/news.php?entrant=1",
                     "http://www.disim.univaq.it/main/news.php?entrant=2")

    news = []
    for url in news_urls:
        soup = utils.get_soup_from_url(url)
        post_items = soup.find_all(class_='post_item_list')
        post_descs = soup.find_all(class_='post_description')
        for i, post_item in enumerate(post_items):
            news.append({
                "title": post_item.h3.a.text,
                "link": "http://www.disim.univaq.it/main/" + post_item.a.get('href'),
                "description": post_descs[i].get_text().replace("\n", " ")
            })
    return news

def check_news():
    """This function check if there are some unread news from the website"""

    pulled_news = pull_news(5)
    stored_news = utils.read_json("json/news.json")
    unread_news = []

    if pulled_news:
        for single_pulled in pulled_news:
            counter = 0
            for single_stored in stored_news:
                if single_pulled:
                    if single_pulled == single_stored:
                        counter += 1

            if counter == 0:
                unread_news.append({key: single_pulled[key] for key in
                                    ('title', 'description', 'link')})

    return unread_news

def create_news_json():
    """Defining command to check (and create) the news.json file"""

    if not os.path.isfile("json/news.json"):
        utils.write_json(pull_news(10), "json/news.json")
