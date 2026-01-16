import mercadopago
from django.conf import settings
from django.urls import reverse
from decimal import Decimal

try:
    MP_SDK = mercadopago.SDK(settings.MP_ACCESS_TOKEN)
except AttributeError:
    MP_SDK = None


def create_mp_preference(order, request, order_items_list):
    if not MP_SDK:
        return None

    if not order_items_list:
        print("ERRO: order_items_list está vazia.")
        return None
        
    total_compra = float(order.total)
    
    items_mp = []
    for item in order_items_list: 
        items_mp.append({
            "title": item.product.name,
            "quantity": item.quantity,
            "unit_price": float(item.unit_price), 
        })
         
    notification_url = request.build_absolute_uri(reverse('payment:mp_webhook')) 
    base_url = "http://127.0.0.1:8000"
    pedido_confirmado_path = reverse('store:pedido_confirmado').lstrip('/')

    preference_data = {
        "items": items_mp,
        "external_reference": str(order.id_order), 
        "back_urls": {
            "success": base_url + "/" + pedido_confirmado_path,
            "pending": base_url + "/" + pedido_confirmado_path,
            "failure": base_url + "/" + pedido_confirmado_path,
        },
        "payer": {
            "email": order.user.email,
        }
    }
    
    preference = MP_SDK.preference().create(preference_data)

    if preference and preference.get('response', {}).get('init_point'):
        return {
            "id": preference['response']['id'],
            "init_point": preference['response']['init_point']
        }
    else:
        error_details = preference.get('response', {}).get('message') 
        print(f"Erro ao criar preferência no Mercado Pago: {error_details}")
        return None
