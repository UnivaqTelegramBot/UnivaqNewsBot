#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""This script scrapes information about the student service office from the univaq website."""

import sys
sys.path.insert(0, '../')
from libs.utils import utils

student_office_url = 'http://www.univaq.it/section.php?id=607'

def scrape_student_office():
    """Get info about the student service office"""

    soup = utils.get_soup_from_url(student_office_url)
    if not soup:
        return
    area = soup.find(text='AREA SCIENTIFICA').parent.parent.find_next_sibling()
    address, phone, email, hours = area.find_all(class_='address_table_description')
    scraped_info = {
        'indirizzo': address.text,
        'telefono': phone.text,
        'e-mail': email.text,
        'orari': hours.text.strip().replace('13', '13, ')
    }
    utils.write_json(scraped_info, '../json/student_office.json')

if __name__ == '__main__':
    scrape_student_office()
