# TUTORIAL
## Como adicionar uma autenticação ao seu aplicativo com o Flask-Login

Por Anthony Herbert

em https://www.digitalocean.com/community/tutorials/how-to-add-authentication-to-your-app-with-flask-login-pt

---
## Objetivo Geral
Permitir que usuários façam login em seu aplicativo é um dos recursos mais comuns
a ser adicionado ao seu aplicativo Web. Este artigo irá abordar como adicionar uma
autenticação ao seu aplicativo Flask com o pacote Flask-Login.

## Objetivos específicos:
- Como usar a biblioteca Flask-Login para o gerenciamento de sessão
- Como usar o utilitário integrado do Flask para o hash de senhas
- Como adicionar páginas protegidas ao nosso aplicativo acessíveis somente por usuários autenticados
- Como usar o Flask-SQLAlchemy para criar um modelo de usuário
- Como criar formulários de inscrição e login para que nossos usuários criem contas e façam login
- Como exibir mensagens de erro aos usuários quando algo der errado
- Como usar informações da conta do usuário para exibi-las na página do perfil


## Estrutura do projeto
    .
    ├── flask_auth_app                 # Pacote do projeto
    │   ├── auth.py              # Blueprint autenticação
    │   ├── db.sqlite            # DB SQLite
    │   ├── __init__.py          # Configuração do app
    │   ├── main.py              # Blueprint principal
    │   ├── models.py            # Modelos de dados para SQLAlchemy
    │   └── templates            # diretório de templates
    │       ├── base.html        # Layout do projeto
    │       ├── index.html       # View para página index
    │       ├── login.html       # View para página login
    │       ├── profile.html     # View para página profile
    │       └── signup.html      # View para página signup
    ├── main.py                        # Script de inicialização via python
    ├── poetry.lock                    # Fix de pacotes poetry
    ├── pyproject.toml                 # Definições do projeto
    └── README.md                      # README com detalhes

## Variaveis de ambiente

Crie o arquivo .env da seguinte forma:

    cat > .env << eof
    FLASK_APP=flask_auth_app
    FLASK_DEBUG=1
    eof


## Banco de dados da aplicação
Os comandos abaixo são para manipulação do
Sistema Gerenciador de Banco de Dados (SGBD), que para este projeto utiliza-se o SQLite.
O banco de dados (DB) precisa ser inicializado na primeira utilização da aplicação.

### Iniciar BD
Esta aplicação utiliza o padrão Factory, e para carregamento do DB via flask-sqlalchemy,
com as devidas configurações proceda com as instruções abaixo:

    poetry shell
    python
    from project import db, create_app
    db.create_all(app=create_app())

### remover BD
Se for necessário, para remover as tabelas, execute os comandos a seguir:

    poetry shell
    python
    from project import db, create_app
    db.drop_all(app=create_app())


## Conclusão
Foi utilizado neste tutorial os pacotes Flask-Login e o Flask-SQLAlchemy para
construir um sistema de login para o nosso aplicativo e abordamos como autenticar
um usuário. Primeiro, criamos um modelo de usuário e armazenamos suas
informações. Em seguida, foi necessário verificar se a senha do usuário estava
correta utilizando o hash na senha do formulário e comparando-a com a armazenada
no banco de dados. Por fim, adicionamos a autorização ao nosso aplicativo usando
o decorador @login_required em uma página de perfil para que apenas usuários
conectados possam ver essa página.

Este tutorial será o suficiente para aplicativos menores, mas se o intúito é
ter mais funcionalidades logo no início, considere usar as bibliotecas
Flask-User ou Flask-Security, que são desenvolvidas com base na biblioteca
Flask-Login.
