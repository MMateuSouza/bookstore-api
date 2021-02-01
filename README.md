# Bookstore API

**Bookstore API** é uma API desenvolvida utilizando a linguagem de programação _Python_, o _Microframework Flask_, e o SGBD _PostgreSQL_. O seu objetivo é ilustrar o contexto de uma Livraria, onde temos Clientes, Livros e Vendas, ou seja, esta aplicação provê uma interface para leitura, cadastro, edição e exclusão de informações pertinentes a essas entidades.

---

## Pré-requisitos

Antes de mais nada, é preciso efetuar a instalação de algumas dependências para este projeto.

* _PostgreSQL_: [Clique Aqui](https://www.postgresql.org/download/) para acessar o site oficial com o passo a passo para instalação.
* _Python 3_: [Clique Aqui](https://www.python.org/) para acessar o site oficial com o passo a passo para instalação.

O projeto foi desenvolvido utilizando o S.O. Ubuntu 18.04.5, caso você esteja utilizando ele ou alguma distribuição Linux baseada em _Debian_ siga o passo a passo abaixo (Caso você esteja utilizando Windows, apenas pule o Passo nº 1):

1. Execute o comando abaixo para instalar algumas dependências para o projeto:
   ```shell
   sudo apt install python3-pip python3-dev python3-venv libpq-dev -y
   ```

2. Agora será necessário efetuar o Download ou clone da aplicação, para isso [clique aqui](https://github.com/MMateuSouza/bookstore-api/archive/master.zip), ou:

   ```shell
   git clone https://github.com/MMateuSouza/bookstore-api.git
   ```

3. Se você efetuou o _download_ pelo link, extraia a pasta e acesse ela. Se você efetuou o _clone_, apenas acesse o diretório.


4. Será necessário criar um ambiente virtual _Python_, para isso (Esteja no diretório do projeto):

    4.1. Linux:
   ```shell
   python -m venv Bookstore
   ```
    4.2. Windows:
   ```shell
    C:\Users\User\Documents\bookstore-api>python -m venv Bookstore
   ```
    `Bookstore` é o nome do seu ambiente virtual _Python_, pode ser qualquer nome que você deseje.

   Observe que foi criada uma pasta chamada `Bookstore` no diretório.


5. E ativar o ambiente virtual _Python_ criado, para isso:
   
   5.1. Linux:
   ```shell
   source Bookstore/bin/activate
   ```
   5.2. Windows:
   ```shell
   Bookstore\Scripts\activate.bat
   ```
   
   Note que há um _feedback_ no terminal parecido com isso:
   ```shell
   (Bookstore) user@DESKTOP-4K7A3QK:~/bookstore-api$
   ```


6. Depois de ativado, é necessário instalar as dependências _Python_ para esse projeto:
   ```shell
   pip install -e .
   ```

7. Ao instalar, execute o seguinte comando para verificar se todas as dependências foram instaladas:
   ```shell
   pip list
   ```
   
   E você deverá ter um feedback parecido com esse:

   ```shell
   (Bookstore) C:\Users\User\Documents\bookstore-api>pip list
   Package          Version Location
   ---------------- ------- ---------------------------------------
   bookstore-api    0.0.0   c:\users\user\documents\bookstore-api
   click            7.1.2
   Flask            1.1.2
   Flask-Cors       3.0.10
   Flask-SQLAlchemy 2.4.4
   itsdangerous     1.1.0
   Jinja2           2.11.3
   MarkupSafe       1.1.1
   pip              20.2.3
   psycopg2         2.8.6
   python-dotenv    0.15.0
   setuptools       49.2.1
   six              1.15.0
   SQLAlchemy       1.3.22
   Werkzeug         1.0.1
   WARNING: You are using pip version 20.2.3; however, version 21.0.1 is available.
   You should consider upgrading via the 'c:\users\user\documents\bookstore-api\bookstore\scripts\python.exe -m pip install --upgrade pip' command.
   
   (Bookstore) C:\Users\User\Documents\bookstore-api>   
   ```
   
8. Temos todas as dependências _Python_ configuradas para o projeto, agora o próximo passo é acessar o _PostgreSQL_ e criar um usuário bem como um banco de dados para a aplicação. Para isso:

   8.1. Linux:
   
   Alterar o usuário corrente para o usuário postgres, caso solicite a senha, informe-a.
   ```shell
   sudo su postgres;
   ```
   
   Acessar o CLI do Postgres.
   ```shell
   psql
   ```
   
   Criar um novo usuário:
   ```postgresql
   CREATE USER bookstore_api_user WITH PASSWORD '<YOUR_PASSWORD>' SUPERUSER;
   ```
   
   E após isso o banco de dados:

   ```postgresql
   CREATE DATABASE bookstore_api_db;
   ```
   
   Para sair do CLI do _Postgres_ é só digitar `exit;`. E para sair do usuário `postgres` é só digitar `exit;` novamente.

   8.2. Windows:
   
   Você irá procurar um programa chamado `SQL Shell (psql)`, ele estará solicitando algumas informações, aperte `Enter` até chegar a opção `Password for user postgres` e você informa a senha colocada no momento da instalação.

   Após isso, basta executar o seguinte comando para criar o banco de dados:
   ```postgresql
   CREATE DATABASE bookstore_api_db;
   ```
   
   Para sair basta fechar a janela.


9. No diretório do projeto existe um arquivo chamado `.env_example`, ele é utilizado como base para gerar um arquivo de configuração de algumas variáveis da aplicação, para criar uma cópia dele:

   9.1. Linux:
   ```shell
   cp .env_example .env
   ```
   9.2. Windows:
   ```shell
   copy .env_example .env
   ```

   O arquivo `.env` se parece um pouco com isso:

   ```shell
   (Bookstore) user@DESKTOP-4K7A3QK:~/bookstore-api$ cat .env
   FLASK_ENV=[development|production|testing]
   DATABASE_URI=postgres://[user]:[password]@[hostname]:[port]/[database]
   MAX_BOOKS_PER_SALE=10
   ```
   
10. Após efetuado a cópia, utilizando um editor de texto de sua preferência abra o arquivo e configure de acordo com a tabela a seguir:

      | # | Field              | Description                                                                                                                                                                                               | DataType | Required |
      |:-:|--------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------:|:--------:|
      | 1 | FLASK_ENV          | Define em qual ambiente a aplicação estará funcionando. Dependendo do valor existem alguns recursos que facilitam o desenvolvimento ou teste. Possíveis valores: `development`, `production` e `testing`. |  String  |   true   |
      | 2 | DATABASE_URI       | Especifica a URL de conexão com o banco de dados. Basta seguir o padrão: `postgres://[user]:[password]@[hostname]:[port]/[database]`.                                                                     |  String  |   true   |
      | 3 | MAX_BOOKS_PER_SALE | Define qual a quantidade de livros distintos podem ser adquiridos por cada Compra. De acordo com a regra de negócio do projeto, o padrão é `10`.                                                          |  Integer |   true   |

11. Depois de tudo configurado, basta executar o seguinte passo a passo para criação das tabelas do banco e inserção da carga inicial do banco:
    
    11.1. Acessar o _shell_ interativo do _Python_:
    ```shell
    python
    ```
   
    11.2. Importar a instância do _SQLAlchemy_ da aplicação:
    
    ```python
    from bookstore_api import db
    ```
    11.3 Criar todas as tabelas necessárias da aplicação:
    
    ```python
    db.create_all()
    ```
    
    11.4. Importar a função de inserção de dados iniciais:
    
    ```python
    from initial_data import insert
    ```
    11.5 Executar método de inserção:
    
    ```python
    insert()
    ```

12. Para executar a API, você precisa exportar uma variável de ambiente que diga ao Flask onde encontrar a instância da aplicação, para isso:
    
    12.1. Linux:
    ```shell
    export FLASK_APP=bookstore_api
    ```
    12.2. Windows:
    ```shell
    set FLASK_APP=bookstore_api
    ```

13. Para executar a aplicação basta executar o seguinte comando:
    
    ```shell
    flask run
    ```
    OU, para rodar um servidor local:
    ```shell
    flask run --host=0.0.0.0
    ```
    
    Caso tenha dado tudo certo, você terá um _feedback_ parecido com esse:
    
    ```shell
    (Bookstore) user@DESKTOP-4K7A3QK:~/bookstore-api$ flask run --host=0.0.0.0
    * Serving Flask app "bookstore_api" (lazy loading)
    * Environment: development
    * Debug mode: on
    * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
    * Restarting with stat
    * Debugger is active!
    * Debugger PIN: 259-854-158
    ```
   
---

## Documentação da API

A aplicação está divida em três módulos: a Clientes, a Livros e a Vendas. Para acessar a documentação de cada módulo, basta selecionar abaixo a desejada.

- **Módulo Clientes:** [Clique aqui](docs/Customer.md), caso queira conhecer como criar, editar, listar e excluir um cliente.
- **Módulo Livros:** [Clique aqui](docs/Book.md), caso queira conhecer como criar, editar, listar e excluir um livro.
- **Módulo Vendas:** [Clique aqui](docs/Sale.md), caso queira conhecer como criar e listar vendas.