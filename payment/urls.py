# payment/urls.py

from django.urls import path
from . import views

app_name = 'payment' 

urlpatterns = [
    path('iniciar/', views.iniciar_pagamento_view, name='iniciar_pagamento'), 
    
    path('webhook/', views.mp_webhook_view, name='mp_webhook'), 
]