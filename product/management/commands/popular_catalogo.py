from django.core.management.base import BaseCommand
from django.db import transaction

from product.catalogo import PRODUTOS_INICIAIS
from product.models import Product


class Command(BaseCommand):
    help = 'Cadastra cafés, kits e opções do clube sem duplicar ou sobrescrever produtos.'

    @transaction.atomic
    def handle(self, *args, **options):
        criados = 0
        for nome, descricao, preco, categoria in PRODUTOS_INICIAIS:
            _, criado = Product.objects.get_or_create(
                name=nome,
                defaults={
                    'description': descricao,
                    'price': preco,
                    'fk_category_id': categoria,
                },
            )
            criados += int(criado)
            self.stdout.write(f'{"Criado" if criado else "Preservado"}: {nome}')
        self.stdout.write(self.style.SUCCESS(f'{criados} produtos criados.'))
