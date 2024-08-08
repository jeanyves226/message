import json
from .utils import sendWhatsAppMessage
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse

@csrf_exempt
def whatsAppWebhook(request):
    if request.method == 'GET':
        VERIFY_TOKEN = '3fafe3de-86c0-41d7-8cba-49a8cd1b993b'
        mode = request.GET['hub.mode']
        token = request.GET['hub.verify_token']
        challenge = request.GET['hub.challenge']

        if mode == 'subscribe' and token == VERIFY_TOKEN:
            return HttpResponse(challenge, status=200)
        else:
            return HttpResponse('Error, invalid token', status=403)

    if request.method == 'POST':
        data= json.loads(request.body)
        if 'object' in data and 'entry' in data:
            if data['object'] == 'whatsapp_business_account':
                try:
                    for entry in data['entry']:
                        pohoneNumber = entry['changes'][0]['value']['metadata']['display_phone_number']
                        phoneId = entry['changes'][0]['value']['metadata']['phone_number_id']
                        profileName = entry['changes'][0]['value']['contacts'][0]['profile']['name']
                        whatAppId = entry['changes'][0]['value']['contacts'][0]['wa_id']
                        fromId = entry['changes'][0]['value']['messages'][0]['from']
                        messageId = entry['changes'][0]['value']['messages'][0]['id']
                        timestamp = entry['change'][0]['value']['messages'][0]['timestamp']
                        text = entry['change'][0]['value']['messages'][0]['text']['body']

                        phoneNumber = "22673340251"
                        message = 'RE: {} was received'.format(text)
                        sendWhatsAppMessage(phoneNumber, message)
                except:
                    pass
        return HttpResponse('Success', status=200)

    return render(request, 'whatsapp.html')