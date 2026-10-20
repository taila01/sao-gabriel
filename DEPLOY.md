# Deploy Django / Vercel

## Driver do banco

O projeto usa `mysql-connector-python==9.7.0` com o backend
`sao_gabriel.db.backends.mysql` (baseado em `mysql.connector.django`) e `use_pure=True`. Não depende de `mysqlclient`,
`PyMySQL` ou bibliotecas nativas de MySQL/MariaDB para compilação.

O driver foi instalado em Python 3.12 com Django 5.2.8, e a inicialização
WSGI e as verificações do Django foram executadas localmente.

## Configuração na Vercel

Em **Settings > Environment Variables**, configure para Production:

- `DB_HOST`: endereço de um banco acessível pela aplicação hospedada.
- `DB_PORT`: porta do banco, geralmente `3306`.
- `DB_NAME`: nome do banco existente.
- `DB_USER`: usuário do banco.
- `DB_PASSWORD`: senha do banco.
- `DB_SSL_CA`: `ca.pem` (certificado CA público baixado da Aiven e incluído no deploy).
- `DJANGO_DEBUG`: `False`.
- `DJANGO_ALLOWED_HOSTS`: `sao-gabriel-blue.vercel.app` ou uma lista de hosts separados por vírgula.

O certificado habilita TLS com validação da CA e da identidade do servidor.
O `.env` local é carregado automaticamente, mas variáveis do ambiente da hospedagem
têm prioridade. Não envie o `.env` ao GitHub.

O host de preview em `VERCEL_URL` também é aceito quando fornecido pela Vercel.
O servidor de banco deve permitir conexões do ambiente hospedado. `localhost`
na Vercel não aponta para o banco da sua máquina.

Depois de enviar o código ao GitHub, acompanhe o novo deployment e os Runtime Logs.
Alterar apenas variáveis de ambiente exige um novo deployment para aplicá-las.
Se houver `pyproject.toml` e `uv.lock` em outra branch/pasta configurada como Root
Directory, alinhe as dependências e regenere o lockfile nessa origem; este checkout
usa `requirements.txt` e não contém esses arquivos.

Não execute migrações automaticamente no build ou a cada requisição. A aplicação
precisa de um banco com as migrações aplicadas em uma etapa de administração separada.

## Verificação local

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python manage.py check
```

Esses checks validam a inicialização e a configuração do Django, não a conexão
com o banco de produção, os pagamentos ou o funcionamento completo do site.

Documentação do backend: https://dev.mysql.com/doc/connector-python/en/connector-python-django-backend.html

O backend local corrige a citação de literais no editor de schema do Connector/Python
9.7.0, necessária para a constraint de UID não vazio do social-auth. As migrações
de terceiros não são alteradas ou marcadas artificialmente como aplicadas.

## Catálogo demonstrativo

Execute `.venv/bin/python manage.py popular_catalogo` para cadastrar quatro cafés,
dois kits e três opções do clube. O comando preserva produtos existentes e pode
ser executado novamente sem duplicar os nomes cadastrados. Categorias: 1 = cafés,
2 = kits, 3 = clube. Os itens e preços são demonstrativos; a compra de um plano
no carrinho representa um ciclo e não ativa cobrança recorrente.
