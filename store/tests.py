from decimal import Decimal
from unittest.mock import patch

from django.template.loader import render_to_string
from django.test import RequestFactory, SimpleTestCase, override_settings
from django.urls import reverse

from product.models import Product


@override_settings(ALLOWED_HOSTS=['testserver'])
class NavegacaoClubeTests(SimpleTestCase):
    def setUp(self):
        self.plano = Product(
            id_product=7, name='Clube Básico', price=79.90, fk_category_id=3,
        )

    @patch('store.views.planos_do_clube')
    def test_clube_mostra_conteudo_e_destino_sem_promessas_nao_implementadas(self, planos):
        planos.return_value = [self.plano]
        response = self.client.get(reverse('store:clube'))
        self.assertContains(response, '250g por mês')
        self.assertContains(response, reverse('product:detalhe_produto', args=[7]))
        self.assertContains(response, 'Renovação mensal automática')
        self.assertNotContains(response, '10%')
        self.assertNotContains(response, 'Frete grátis no Sudeste')
        self.assertContains(response, reverse('store:ajuda'))

    @patch('store.views.planos_do_clube', return_value=[])
    def test_sem_planos_nao_mostra_preco_ou_compra_inexistente(self, planos):
        response = self.client.get(reverse('store:clube'))
        self.assertContains(response, 'Os planos estão sendo preparados.')
        self.assertNotContains(response, 'R$ 79,90')

    def test_ajuda_esclarece_limites_de_entrega_e_recorrencia(self):
        response = self.client.get(reverse('store:ajuda'))
        self.assertContains(response, 'Ainda não há entrega real')
        self.assertContains(response, 'a renovação é automática')

    def test_carrinho_mostra_foto_e_preserva_controles(self):
        request = RequestFactory().get('/carrinho/')
        request.session = {}
        item = {
            'produto': self.plano, 'produto_id': 7, 'quantidade': 1,
            'preco_unitario': Decimal('79.90'), 'subtotal_item': Decimal('79.90'),
        }
        html = render_to_string('carrinho.html', {
            'itens': [item], 'subtotal': Decimal('79.90'),
            'frete': 0, 'total_compra': Decimal('79.90'),
        }, request=request)
        self.assertIn(reverse('product:imagem_catalogo', args=['clube-v2']), html)
        self.assertIn(reverse('store:aumentar_quantidade', args=[7]), html)
        self.assertIn(reverse('store:remover_produto', args=[7]), html)
