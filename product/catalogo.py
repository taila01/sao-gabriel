"""Categorias e opções demonstrativas do catálogo São Gabriel."""

CAFE = 1
KIT = 2
CLUBE = 3

PRODUTOS_INICIAIS = [
    ('Café Ritual — 250g', 'Café em grãos, torra média, embalagem de 250g. Produto demonstrativo do catálogo São Gabriel.', 34.90, CAFE),
    ('Café Amanhecer — 250g', 'Café moído para filtro, torra média, embalagem de 250g. Produto demonstrativo do catálogo São Gabriel.', 32.90, CAFE),
    ('Café Encontro — 500g', 'Café em grãos, torra média, embalagem de 500g. Produto demonstrativo do catálogo São Gabriel.', 59.90, CAFE),
    ('Café Pausa — 500g', 'Café moído para filtro, torra média, embalagem de 500g. Produto demonstrativo do catálogo São Gabriel.', 54.90, CAFE),
    ('Kit Descoberta — 2 cafés de 250g', 'Duas embalagens de 250g: Café Ritual em grãos e Café Amanhecer moído. Kit demonstrativo para conhecer as opções do catálogo.', 64.90, KIT),
    ('Kit Compartilhar — 2 cafés de 500g', 'Duas embalagens de 500g: Café Encontro em grãos e Café Pausa moído. Kit demonstrativo para compartilhar.', 109.90, KIT),
    ('Clube Básico', 'Opção demonstrativa do clube: 250g de café por ciclo mensal. Valor de referência por ciclo: R$ 79,90. A compra pelo carrinho não ativa cobrança recorrente.', 79.90, CLUBE),
    ('Clube Premium', 'Opção demonstrativa do clube: 500g de café por ciclo mensal, em duas embalagens de 250g. Valor de referência por ciclo: R$ 129,90. A compra pelo carrinho não ativa cobrança recorrente.', 129.90, CLUBE),
    ('Clube Master', 'Opção demonstrativa do clube: 1kg de café por ciclo mensal, em duas embalagens de 500g. Valor de referência por ciclo: R$ 199,90. A compra pelo carrinho não ativa cobrança recorrente.', 199.90, CLUBE),
]


# Informações das opções demonstrativas cadastradas pelo projeto.
INFORMACOES_PRODUTOS = {
    'Café Ritual — 250g': {'peso': '250g', 'apresentacao': 'Em grãos', 'torra': 'Média'},
    'Café Amanhecer — 250g': {'peso': '250g', 'apresentacao': 'Moído para filtro', 'torra': 'Média'},
    'Café Encontro — 500g': {'peso': '500g', 'apresentacao': 'Em grãos', 'torra': 'Média'},
    'Café Pausa — 500g': {'peso': '500g', 'apresentacao': 'Moído para filtro', 'torra': 'Média'},
    'Kit Descoberta — 2 cafés de 250g': {'peso': '500g no total', 'apresentacao': '1 Ritual em grãos + 1 Amanhecer moído', 'torra': 'Média', 'conteudo': '2 embalagens de 250g'},
    'Kit Compartilhar — 2 cafés de 500g': {'peso': '1kg no total', 'apresentacao': '1 Encontro em grãos + 1 Pausa moído', 'torra': 'Média', 'conteudo': '2 embalagens de 500g'},
    'Clube Básico': {'peso': '250g por ciclo', 'conteudo': '1 embalagem de 250g', 'rotulo': 'Básico', 'chamada': 'Para começar'},
    'Clube Premium': {'peso': '500g por ciclo', 'conteudo': '2 embalagens de 250g', 'rotulo': 'Premium', 'chamada': 'Para explorar'},
    'Clube Master': {'peso': '1kg por ciclo', 'conteudo': '2 embalagens de 500g', 'rotulo': 'Master', 'chamada': 'Para compartilhar'},
}
