from urllib.request import urlopen
import json
from config import *

def get_data():
    url = "https://www.fio.cz/ib_api/rest/last/{token}/transactions.json"
    response = urlopen(url.format(token=FIO_TOKEN), timeout=120).read()
    encoding = response.info().get_content_charset('utf-8')
    data = json.loads(response.decode(encoding))
    transactions = data["accountStatement"]["transactionList"]["transaction"]

    incoming_transactions = []
    parsed_transactions = []

    for transaction in transactions:
        if transaction["column1"]["value"] > 0:
            incoming_transactions.append(transaction)
    
    for transaction in incoming_transactions:
        if transaction["column7"] != None:
            parsed = {}
            parsed["name"] = transaction["column7"]["value"]
            parsed["volume"] = transaction["column1"]["value"]
            parsed["identification"] = transaction["column5"]["value"] if transaction["column5"] != None else None
            parsed["currency"] = transaction["column14"]["value"].upper()
            parsed["message"] = transaction["column16"]["value"] if transaction["column16"] != None else None
            parsed_transactions.append(parsed)

    return parsed_transactions
