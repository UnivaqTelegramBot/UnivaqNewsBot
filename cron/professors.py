#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""This script scrapes all the professors from the univaq website."""

import sys
sys.path.insert(0, '../')
from libs.utils import utils

def courses_cleanup(s):
    return ', '.join([x for x in s.splitlines() if x and x[0] != u'\xa0'])

def email_soup_cleanup(email_soup):
    if not email_soup.a:
        return ''
    email_soup.find('img', alt='at').replace_with('@')
    for img in email_soup.find_all('img'):
        img.replace_with('.')
    return email_soup.text.strip()  # .lower()  # ?

def phone_cleanup(s):
    if not s:
        return ''
    s = ''.join([c for c in s if c.isdigit() or c == '+'])
    if s and s[0] != '+' and len(s) == 10:
        s = '+39' + s  # if not already internationalized, make it Italian
    return '-'.join([s[:3], s[3:7], s[7:]]) if s.startswith('+39') else s

def scrape_professors():
    """Get information about professors"""

    professors_url = ("http://www.disim.univaq.it/didattica/"
                      "content.php?tipo=3&ordine=1&chiave=0&pid=25&did=8&lid=it&"
                      "frmRicercaNome=&frmRicercaCognome=&frmRicercaLaurea=1&action_search=Filtra")
    soup = utils.get_soup_from_url(professors_url)
    professor_names = soup.find("table").find_all(colspan='2')
    scraped_professors = []
    for name_cell in professor_names:
        name, phone, email, courses, _ = name_cell.parent.find_all('td')
        scraped_professors.append({
            "nome": name.text or "non disponibile",
            "telefono": phone_cleanup(phone.text) or "non disponibile",
            "e-mail": email_soup_cleanup(email) or "non disponibile",
            "corsi": courses_cleanup(courses.text) or "non disponibile",
            # "ufficio": "0"  # why provide useless data??
        })
    utils.write_json(scraped_professors, "../json/professors.json")

if __name__ == "__main__":
    scrape_professors()
