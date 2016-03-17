#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""This script scrapes information about the student service office from the univaq website."""

import bs4
import requests
import sys
sys.path.insert(0, '../')
from libs.utils import utils

student_office_url = 'http://www.univaq.it/section.php?id=607'

def get_soup_from_url(url):
    """Download a webpage and return its BeautifulSoup"""

    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5)',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'accept-charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'accept-encoding': 'gzip,deflate,sdch',
        'accept-language': 'en-US,en;q=0.8',
    }
    request = requests.get(url, headers=headers)
    if request.status_code == 200:
        return bs4.BeautifulSoup(request.text, 'html.parser')
    else:
        print('Error! Status ' + request.status_code)
        return None

def scrape_student_office():
    """Get info about the student service office"""

    soup = get_soup_from_url(student_office_url)
    if not soup:
        return
    first_row = soup.find(string='AREA SCIENTIFICA').parent.parent.find_next_sibling()
    address, phone, email, hours = first_row.find_all(class_='address_table_description')
    scraped_info = {
        'indirizzo': address.text,
        'telefono': phone.text,
        'e-mail': email.text,
        'orari': hours.text.strip().replace('13', '13, ')
    }
    utils.write_json(scraped_info, '../json/student_office.json')

if __name__ == '__main__':
    scrape_student_office()
