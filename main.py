# -*- coding: utf-8 -*-
import locale
import mail
import fio
import secrets

locale.setlocale(locale.LC_ALL, secrets.LOCALE)
title = u'FIO Bank příchozí platby'
text = ''

transactions = fio.get_data()

for transaction in transactions:
    text += u'Jméno: {name}\n'.format(name=transaction['name'])
    text += u'Částka: {volume}{currency}\n'.format(volume=locale.currency(transaction['volume'], False, True).replace('\xa0', ' '), currency=transaction['currency'])
    if transaction['identification'] != None:
        text += u'VS: {identification}\n'.format(identification=transaction['identification'])
    if transaction['message'] != None:
        text += u'Zpráva pro příjemce: {message}\n'.format(message=transaction['message'])
    text += '\n'

if len(transactions) > 0:
    mail.send_mail(title, text)