from django.urls import path
from . import views

urlpatterns = [
    path('9e3c226f-d6d8-4e40-afba-00881daf30b7', views.whatsAppWebhook, name='whatsapp-webhook'),

]