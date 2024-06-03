# Minha Aplicação de CRUD com Flask e MongoDB

Este é um projeto simples de uma aplicação CRUD (Create, Read, Update, Delete) criada com Flask e MongoDB. A aplicação permite gerenciar uma coleção de produtos.

## Funcionalidades

- **Criar**: Adicione novos produtos à coleção.
- **Ler**: Consulte a lista completa de produtos ou um produto específico por ID.
- **Atualizar**: Edite o título de um produto existente.
- **Excluir**: Remova produtos da coleção.

## Pré-requisitos

Antes de começar, certifique-se de ter as seguintes dependências instaladas:

- Python 3.x
- Flask 2.2.2
- PyMongo 4.3.3

## Instalação

1. Clone o repositório para sua máquina:

   ```bash
   git clone https://github.com/alan-vieira/api_crud_flask_com_mongodb.git

2. Instale as dependências Python listadas no arquivo

   `requirements.txt`:

   ```bash
   pip install -r requirements.txt

3. Configure a variável `mongopass` no arquivo `app.py` com sua URI de conexão MongoDB. *JÁ ESTÁ CONFIGURADO*

## Uso

1.  Inicie o servidor Flask:

    ```bash
    python app.py
 
2. Use cURL ou uma ferramenta similar para realizar operações CRUD, conforme descrito no README anterior.

OBS: Comandos cURL está no txt!
