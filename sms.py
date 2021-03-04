import json
from http.client import HTTPSConnection
from config import *

def send_sms(text):
    for number in BULKGATE_TO:
        print("Sending SMS request to %s" % number)
        connection = HTTPSConnection("portal.bulkgate.com")
        connection.request("POST", "/api/1.0/simple/transactional", json.dumps({
            "application_id": BULKGATE_ID,
            "application_token": BULKGATE_TOKEN,
            "number": number,
            "text": text,
            "sender_id": "gText",
            "sender_id_value": BULKGATE_SENDER,
            "unicode": True
        }), {
            "Content-type": "application/json"
        })
        response = connection.getresponse()
        print("Response: %s" % response.read().decode())
