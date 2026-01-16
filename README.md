# ☕ São Gabriel – E-commerce de Cafés e Assinaturas

## 📌 Descrição

O **São Gabriel** é um projeto de **e-commerce de cafés especiais e planos de assinatura**, desenvolvido com **Django** no backend e **HTML + TailwindCSS** no frontend.

A aplicação permite que usuários se cadastrem, gerenciem seus endereços, adicionem produtos ao carrinho e finalizem compras com **integração à API do Mercado Pago**.
Na área administrativa, é possível realizar **CRUD de produtos** e **atualizar o status dos pedidos**.

---

## 🚀 Tecnologias Utilizadas

* **Python**
* **Django**
* **HTML5**
* **TailwindCSS**
* **MariaDB**
* **API Mercado Pago**

---

## ⚙️ Instalação

### 1️⃣ Clone o repositório

```bash
git clone https://github.com/seu-usuario/sao-gabriel.git
cd sao-gabriel
```

### 2️⃣ Crie e ative o ambiente virtual

```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

### 3️⃣ Instale as dependências

```bash
pip install -r requirements.txt
```

### 4️⃣ Configure o banco de dados (MariaDB)

No arquivo `settings.py`, configure:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'sao_gabriel',
        'USER': 'usuario',
        'PASSWORD': 'senha',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

### 5️⃣ Configure o Mercado Pago

```python
MP_ACCESS_TOKEN = 'SEU_ACCESS_TOKEN'
```

### 6️⃣ Execute as migrações

```bash
python manage.py migrate
```

### 7️⃣ Inicie o servidor

```bash
python manage.py runserver
```

---

## 🛒 Uso

### Usuário

* Criar conta e fazer login
* Atualizar endereço
* Adicionar produtos ao carrinho
* Finalizar compra
* Realizar pagamento via Mercado Pago

### Admin

* Criar, editar e excluir produtos
* Visualizar pedidos
* Atualizar status do pedido

---

## 📂 Estrutura do Projeto

```bash
sao_gabriel/
├── app_admin/
├── store/
├── payment/
├── templates/
├── static/
├── manage.py
└── README.md

## 🛠️ Tecnologias

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge\&logo=python\&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge\&logo=django\&logoColor=white)
![HTML](https://img.shields.io/badge/HTML-E34F26?style=for-the-badge\&logo=html5\&logoColor=white)
![TailwindCSS](https://img.shields.io/badge/TailwindCSS-38B2AC?style=for-the-badge\&logo=tailwind-css\&logoColor=white)
![MariaDB](https://img.shields.io/badge/MariaDB-003545?style=for-the-badge\&logo=mariadb\&logoColor=white)
