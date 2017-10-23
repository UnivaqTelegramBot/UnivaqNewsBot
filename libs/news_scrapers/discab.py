#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The actual scraper of Discab"""

from bs4 import BeautifulSoup
import requests

def general_scraper(section_url):
    """This function is built to have a general news scraper to get news from Discab"""

    prefix = "http://discab.univaq.it/"

    request = []
    bs_list = []
    news = []

    for i, url in enumerate(section_url):
        request.append(requests.get(url))
        bs_list.append(BeautifulSoup(request[i].text, "html.parser")
                       .find_all(class_='avvisi_title')[0:5])

        for single_news in bs_list[i]:
            news.append({
                'description': '',
                'title': single_news.a.string,
                'link': prefix + single_news.a['href']
            })

    return news

def general_news():
    """This function is built to get Discab general news"""

    return general_scraper(['http://discab.univaq.it/index.php?id=2004'])

def biotechnology_news():
    """This function is built to get biotechnology news"""

    return general_scraper(['http://discab.univaq.it/index.php?id=1957'])

def medical_news():
    """This function is built to get medical news"""

    return general_scraper(['http://discab.univaq.it/index.php?id=1958'])

def motor_science_news():
    """This function is built to get motor science news"""

    return general_scraper(['http://discab.univaq.it/index.php?id=2003'])

def psychology_news():
    """This function is built to get psychology news"""

    return general_scraper(['http://discab.univaq.it/index.php?id=2321'])
