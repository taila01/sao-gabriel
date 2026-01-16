from django.db import models

from django.conf import settings

class Pedido(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pendente'),
        ('APPROVED', 'Aprovado'),
        ('REJECTED', 'Rejeitado'),
        ('CANCELLED', 'Cancelado'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)
    
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=30, blank=True)
    endereco = models.TextField(blank=True)
    
    total = models.DecimalField(max_digits=10, decimal_places=2)
    status_pagamento = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    
    external_reference = models.CharField(max_length=255, blank=True)
    mp_payment_id = models.CharField(max_length=100, blank=True)
    mp_status = models.CharField(max_length=50, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Pedido #{self.id} - {self.nome} ({self.status_pagamento})"


class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='itens')
    produto = models.CharField(max_length=100)
    quantidade = models.PositiveIntegerField()
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def subtotal(self):
        return self.quantidade * self.preco_unitario

    def __str__(self):
        return f"{self.quantidade}x {self.produto}"


from django.db import models


from django.conf import settings

class Pedido(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pendente'),
        ('APPROVED', 'Aprovado'),
        ('REJECTED', 'Rejeitado'),
        ('CANCELLED', 'Cancelado'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)
    
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=30, blank=True)
    endereco = models.TextField(blank=True)
    
    total = models.DecimalField(max_digits=10, decimal_places=2)
    status_pagamento = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    
    external_reference = models.CharField(max_length=255, blank=True)
    mp_payment_id = models.CharField(max_length=100, blank=True)
    mp_status = models.CharField(max_length=50, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Pedido #{self.id} - {self.nome} ({self.status_pagamento})"


class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='itens')
    produto = models.CharField(max_length=100)
    quantidade = models.PositiveIntegerField()
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def subtotal(self):
        return self.quantidade * self.preco_unitario

    def __str__(self):
        return f"{self.quantidade}x {self.produto}"
