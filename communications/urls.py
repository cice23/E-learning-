from django.urls import path
from .views import email_webhook, inbox

urlpatterns = [
    path('webhook/', email_webhook, name='email_webhook'),
    path('inbox/', inbox, name='inbox'),
]
