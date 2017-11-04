#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The actual scraper of Discab"""

from bs4 import BeautifulSoup
import requests

def scraper(section_url):
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
