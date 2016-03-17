#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The package that contains groups all the functions needed by other scripts."""

import sys
sys.path.insert(0, '../')

import bs4
import configparser
import json
import logging
import os
import requests


def get_configuration():
    """Get global configuration from service.cfg"""

    config = configparser.ConfigParser()
    config.read("service.cfg")

    return config

def get_logger(debug):
    """Get logger object"""

    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO
        )
    logger = logging.getLogger(__name__)

    if debug is False:
        logging.disable(logging.CRITICAL)

    return logger

def write_json(data, json_file):
    """General function used everywhere to write data into a json file"""

    with open(json_file, "w") as json_file:
        json.dump(data, json_file, indent=4)

def read_json(json_file):
    """General function used everywhere to read a json file"""

    with open(json_file, "r") as json_file:
        return json.load(json_file)

def load_subscribers_json(json_file="json/subscribers.json"):
    """Defining command to check (and create) the subscribers.json file"""

    global SUBSCRIBERS
    SUBSCRIBERS = read_json(json_file) if os.path.isfile(json_file) else []

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
        fmt = 'Error! get_soup_from_url({}) --> Status: {}' 
        print(fmt.format(url, request.status_code))
        return None

