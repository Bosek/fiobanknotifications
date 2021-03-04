import importlib
import locale
import fio
import mail
import config
import sms

locale.setlocale(locale.LC_ALL, config.LOCALE)

transactions = fio.get_data()

if (config.USEMAIL):
    title = u"FIO Bank příchozí platby, účet %s" % config.ACCOUNT_NAME
    text = "Účet %s:\n" % config.ACCOUNT_NAME

    for transaction in transactions:
        text += u"Jméno: %s\n" % transaction["name"]
        text += u"Částka: %s %s\n" % (locale.currency(transaction["volume"], False, True).replace("\xa0", " "), transaction["currency"])
        if transaction["identification"] is not None:
            text += u"VS: %s\n" % transaction["identification"]
        if transaction["message"] is not None:
            text += u"Zpráva pro příjemce: %s\n" % transaction["message"]
        text += "\n"

    if len(transactions) > 0:
        mail.send_mail(title, text)

if (config.USEBULKGATE):
    for transaction in transactions:
        text = "Příchozí platba na účet %s\n" % config.ACCOUNT_NAME
        text += u"Jméno: %s\n" % transaction["name"]
        text += u"Částka: %s %s\n" % (locale.currency(transaction["volume"], False, True).replace("\xa0", " "), transaction["currency"])
        if transaction["identification"] is not None:
            text += u"VS: %s\n" % transaction["identification"]
        if transaction["message"] is not None:
            text += u"Zpráva pro příjemce: %s\n" % transaction["message"][0:20]
        text += "\n"
        sms.send_sms(text)
