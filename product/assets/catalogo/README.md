# Imagens ilustrativas do catálogo

Criadas com a ferramenta integrada `image_gen`, para o catálogo demonstrativo São Gabriel.

- `cafe-v1.png`: uma embalagem de café; categoria 1.
- `kit-v1.png`: duas embalagens de café; categoria 2.
- `clube-v1.png`: caixa com duas embalagens; categoria 3.

As imagens são compartilhadas por categoria e identificadas como ilustrativas na interface.
Não são fotos de produtos reais nem cópias da marca usada como referência pelo usuário.
As rotas `product:imagem_catalogo` servem os arquivos locais sem depender de armazenamento externo.

## Prompts finais

O prompt de cada imagem resulta do texto abaixo, substituindo `{subject}` por uma das descrições seguintes:

```text
Use case: product-mockup. Asset type: square product photograph for a coffee webshop catalog. Subject: {subject}. Original São Gabriel branding, do not copy other brands. Warm cream plaster tabletop and backdrop, sparse scattered roasted coffee beans, subtle blurred olive green coffee foliage in upper corner, soft natural window light and gentle leaf shadows. Photorealistic premium editorial product photography, warm neutral palette, highly realistic paper texture. Product fully visible, centered, occupies 70 percent of square frame, generous margins, cohesive elegant minimal design. No people, no watermarks, no extra props, no prices or unsupported origin/certification claims.
```

### cafe-v1.png

```text
one upright matte ivory resealable coffee bag, delicate forest green label, text only 'SÃO GABRIEL' and 'CAFÉS ESPECIAIS', small line drawing of coffee branch
```

### kit-v1.png

```text
two upright matte ivory coffee bags, one forest green label and one warm caramel label, both read only 'SÃO GABRIEL', arranged together as a coffee gift kit
```

### clube-v1.png

```text
an open kraft subscription box with two ivory coffee bags with forest green labels reading only 'SÃO GABRIEL', thoughtful minimal coffee subscription packaging
```

## Nova imagem do clube

`clube-v2.png` substitui a imagem do clube nas páginas. Criada com a ferramenta
integrada image_gen, preservando `clube-v1.png` como versão anterior.

Prompt final:

```text
Use case: product-mockup. Asset type: square coffee subscription catalog photo, replacement for an overly close cropped box photo. Create original São Gabriel premium coffee subscription packaging. A compact kraft gift box with its lid open, two small matte cream coffee pouches inside, forest green minimal labels with only the exact text 'SÃO GABRIEL'. Camera pulled BACK, a flattering three-quarter angle slightly above tabletop, show the complete box, entire lid and complete pouches with plenty of empty cream background on ALL sides. The entire box and lid must occupy no more than 65 percent of frame width AND height; at least 15 percent clear margins all around. No part cut off, no tall looming lid. Warm ivory tabletop and seamless beige plaster background, very sparse scattered coffee beans and softly blurred green leaves far in background. Soft natural window lighting, elegant subtle leaf shadow, realistic paper texture, refined commercial product photography. Calm warm cream, caramel and forest green palette. No watermarks, no people, no other brands, no certification or origin claims. Square image.
```

`favicon-cafe.svg` é um ícone vetorial de xícara, desenhado em código para a aba do navegador.
