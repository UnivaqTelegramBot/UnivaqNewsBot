#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The Package that contains all the telegram functions used except news"""

import sys
sys.path.insert(0, '../')

from libs.utils import utils

def prof_command(bot, update, args=None):
    """Defining the `prof` command"""

    data = utils.read_json("json/professors.json")
    prof_name = args[0].strip().lower() if args else ''
    if prof_name:
        fmt = '{nome} - {telefono} - {e-mail} - {corsi}\n'
    else:
        fmt = '{nome} - {telefono} - {e-mail}'
    professors = '\n'.join(fmt.format(**prof) for prof in data
                           if prof_name in prof['nome'].lower())

    bot.sendMessage(update.message.chat_id, text=professors + '\n')

def student_office_command(bot, update):
    """Defining the `student_office` command"""

    fmt = 'Orari: {orari}\nIndirizzo: {indirizzo}\nTelefono: {telefono}\nE-mail: {e-mail}'
    student_office_info = fmt.format(**utils.read_json("json/student_office.json"))
    bot.sendMessage(update.message.chat_id, text=student_office_info)

def canteen_command(bot, update):
    """Defining the `canteen` command"""

    canteen_info = 'Orari: {orari}'.format(**utils.read_json("json/mensa.json"))
    bot.sendMessage(update.message.chat_id, text=canteen_info)

def adsu_command(bot, update):
    """Defining the `adsu` command"""

    adsu_info = utils.read_json("json/adsu.json")['info']
    bot.sendMessage(update.message.chat_id, text=adsu_info)
