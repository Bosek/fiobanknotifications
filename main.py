# -*- coding: utf-8 -*-
import mail
import fio

transactions = fio.parsed_transactions
title = u'FIO Bank příchozí platby'
text = ''

for transaction in transactions:
    text += u'Jméno: {name}\nČástka: {volume} Kč\nVS: {identification}\n\n'.format(name=transaction['name'], volume=transaction['volume'], identification=transaction['identification'] if transaction['identification'] != None else u'nezadáno')

mail.send_mail(title, text)