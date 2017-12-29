import urllib2
import json
from secrets import *

url = 'https://www.fio.cz/ib_api/rest/last/{token}/transactions.json'

url = urllib2.urlopen(url.format(token=FIO_TOKEN))
response = url.read()
data = json.loads(response)
transactions = data['accountStatement']['transactionList']['transaction']

incoming_transactions = []
parsed_transactions = []

for transaction in transactions:
    if transaction['column1']['value'] > 0:
        incoming_transactions.append(transaction)

for transaction in incoming_transactions:
    if transaction['column7'] != None:
        parsed = {}
        parsed['name'] = transaction['column7']['value']
        parsed['volume'] = transaction['column1']['value']
        parsed['identification'] = transaction['column5']['value'] if transaction['column5'] != None else None
        parsed_transactions.append(parsed)