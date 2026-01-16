from django.urls import path
from . import views

app_name = 'product' 

urlpatterns = [
    path('', views.listar_produtos, name='listar_produtos'), 
    
    path('<int:product_id>/', views.detalhe_produto, name='detalhe_produto'),
]