#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The actual scraper of the Disim"""

from bs4 import BeautifulSoup
import requests

def scraper():
    """This function is built to pull 5 news from the news page of the disim"""

    # Thanks to Luca Pattavina for giving me the right url
    news_url = ["http://www.disim.univaq.it/main/news.php?entrant=1",
                "http://www.disim.univaq.it/main/news.php?entrant=2"]

    request = []
    bs_list = []
    news = []
    for i, url in enumerate(news_url):
        request.append(requests.get(url))
        bs_list.append(BeautifulSoup(request[i].text, "html.parser")
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
