#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The Package that contains all the telegram's news functions used"""

import sys

from bs4 import BeautifulSoup
import requests

from libs.utils import utils

sys.path.insert(0, '../')

def news_command(bot, update, args):
    """Defining the `news` command"""

    if len(args) and int(args[0]) <= 10:
        news_array = utils.DISIMNEWS[0:int(args[0])]
    else:
        news_array = utils.DISIMNEWS

    news_to_string = ""
    for i, item in enumerate(news_array):
        item["suffix"] = '...' if len(item['description']) > 75 else ''
        news_to_string += str(i+1)+"- [{title}]({link})\n{description:.75}{suffix}\n".format(**item)

    bot.sendMessage(update.message.chat_id, parse_mode='Markdown', text=news_to_string)

def pull_news(num):
    """This function is built to pull 10 (or an arbitrary number) news from the news page"""

    headers = {
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5)",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "accept-charset": "ISO-8859-1,utf-8;q=0.7,*;q=0.3",
        "accept-encoding": "gzip,deflate,sdch",
        "accept-language": "en-US,en;q=0.8",
    }

    # Thanks to Luca Pattavina for giving me the right url
    if num <= 5:
        news_url = ["http://www.disim.univaq.it/main/news.php?entrant=1"]
    else:
        news_url = ["http://www.disim.univaq.it/main/news.php?entrant=1",
                    "http://www.disim.univaq.it/main/news.php?entrant=2"]

    request = []
    bs_list = []
    news = []
    for i, url in enumerate(news_url):
        request.append(requests.get(url, headers=headers))
        bs_list.append(BeautifulSoup(request[i].text, "html.parser") \
                .find_all(class_="post_item_list"))
        descr_list = BeautifulSoup(request[i].text, "html.parser") \
                .find_all(class_="post_description")

        for j, single_news in enumerate(bs_list[i]):
            news.append({
                "title": single_news.h3.a.text,
                "description": descr_list[j].get_text().replace("\n", " "),
                "link": "http://www.disim.univaq.it/main/" + single_news.a.get('href')
            })

    return news

def check_news():
    """This function check if there are some unread news from the website"""

    pulled_news = pull_news(5)
    stored_news = utils.DISIMNEWS
    unread_news = []

    if len(pulled_news) > 0:
        for single_pulled in pulled_news:
            counter = 0
            for single_stored in stored_news:
                if len(single_pulled) > 0:
                    if single_pulled["title"] == single_stored["title"]:
                        counter = counter+1

            if counter == 0:
                unread_news.append({"title": single_pulled["title"],
                                    "description": single_pulled['description'],
                                    "link": single_pulled['link']})

    return unread_news
