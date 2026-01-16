# payment/views.py

from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib import messages
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .services import create_mp_preference 

def iniciar_pagamento_view(request):
    """
    Recebe o ID do Pedido e chama o serviço do Mercado Pago.
    """
    order_id = request.GET.get('order_id')
    
    if not order_id:
        messages.error(request, "ID do pedido não fornecido.")
        return redirect(reverse('store:carrinho')) 
    
    try:
        class MockOrder:
             id_order = order_id
             total = Decimal(request.session.get('total_pedido', '100.00'))
             user = request.user 
        pedido = MockOrder() 

    except Exception: 
        messages.error(request, f"Pedido {order_id} não encontrado.")
        return redirect(reverse('store:carrinho'))

    mp_data = create_mp_preference(pedido, request)
    
    if mp_data and mp_data.get('init_point'):
        return redirect(mp_data['init_point'])
    else:
        messages.error(request, 'Erro ao comunicar com o Mercado Pago. Tente novamente.')
        return redirect(reverse('store:carrinho'))


@csrf_exempt
def mp_webhook_view(request):
    """
    Recebe as notificações de status de pagamento do Mercado Pago (IPN).
    """
    if request.method == 'POST':
        topic = request.GET.get('topic', request.POST.get('topic'))
        resource_id = request.GET.get('id', request.POST.get('id')) 

        if topic and resource_id:
            return HttpResponse(status=200) 
        
    return HttpResponse(status=400)