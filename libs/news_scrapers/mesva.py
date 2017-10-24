#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The actual scraper of Mesva"""

from bs4 import BeautifulSoup
import requests

def general_scraper(section_url):
    """This function is built to have a general news scraper to get news from Mesva"""

    prefix = "http://mesva.univaq.it/"

    request = []
    news = []

    for i, url in enumerate(section_url):
        request.append(requests.get(url))
        news_division = BeautifulSoup(request[i].text, "html.parser").find(class_="view-content")

        discab_news = news_division.find_all("div", recursive=False)[0:5]

        for single_news in discab_news:
            news.append({
                'description': '',
                'title': single_news.a.string,
                'link': prefix + single_news.a['href']
            })

    return news

def general_news():
    """This function is built to get Mesva general news"""

    return general_scraper(['http://mesva.univaq.it/'])

def medical_news():
    """This function is built to get medical news"""

    return general_scraper(['http://mesva.univaq.it/?q=avvisi/cl-clm/52666'])

def environmental_science_news():
    """This function is built to get environmental science news"""

    return general_scraper(['http://mesva.univaq.it/?q=avvisi/cl-clm/52671'])

def biological_science_news():
    """This function is built to get biological science news"""

    return general_scraper(['http://mesva.univaq.it/?q=avvisi/cl-clm/52672'])
