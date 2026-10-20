from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from store.utils.cart_utils import get_cart_data


def listar_produtos(request):
    """
    Exibe a lista de todos os planos de café (Produtos).
    Esta é a view da rota base do app product.
    """
    produtos = Product.objects.all()
    busca = request.GET.get('q', '').strip()
    kits = request.GET.get('tipo') == 'kits'
    if kits:
        produtos = produtos.filter(name__icontains='kit')
    if busca:
        from django.db.models import Q
        produtos = produtos.filter(Q(name__icontains=busca) | Q(description__icontains=busca))

    cart_data = get_cart_data(request)

    context = {
        'produtos': produtos,
        'busca': busca,
        'kits': kits,
        'carrinho_subtotal': cart_data['subtotal']
    }
    return render(request, 'product/listar_produtos.html', context)


def detalhe_produto(request, product_id):
    """
    Exibe a página de detalhes de um único plano de café.
    """
    produto = get_object_or_404(Product, id_product=product_id)
    cart_data = get_cart_data(request)

    context = {
        'produto': produto,
        'carrinho_subtotal': cart_data['subtotal']
    }
    return render(request, 'product/detalhe_produto.html', context)
