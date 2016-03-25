#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""This script scrapes all the info about the adsu of the university's city."""

import sys
sys.path.insert(0, '../')
from libs.utils import utils

adsu_url = "http://www.adsuaq.org/"

def scrape_adsu():
    """Get information about the adsu in a crazy way due to their bitching page made like shit"""

    scraped_info = {}
    soup = utils.get_soup_from_url(adsu_url)
    info = soup.find(id="AutoNumber5").text.splitlines()
    info = '\n'.join(x.strip() for x in info if x.strip())
    info = info.replace('  ', ' ').replace('  :', ':').replace(' :', ':')

    scraped_info.update({
        "info": info
    })

    utils.write_json(scraped_info, "../json/adsu.json")

if __name__ == "__main__":
    scrape_adsu()
