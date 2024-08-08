from django.conf import settings
import requests

def sendWhatsAppMessage(phoneNumber, message):
    headers = {
        "Authorization": settings.WHATSAPP_TOKEN,
        "Content-Type": "application/json"
    }
    payload = {
        "messaging_product": "whatsapp",
        "recipient_type": "individual",
        "to": phoneNumber,
        "type": "text",
        "text": {
            "body": message
        }
    }
    response=requests.post(settings.WHATSAPP_URL, headers=headers, json=payload)
    ans=response.json()
    return ans

#phoneNumber="22675675420"
#message="hello how are you \n this an exemple of message 😁😁 "

#ans = sendWhatsAppMessage(phoneNumber, message)
