# Módulo de Livros

Neste arquivo contém a documentação necessária para a utilização das funcionalidades de criação, leitura, edição e deleção de um Livro.

**Listar Todos os Livros**
----
Retorna um JSON contendo todos os Livros cadastrados no banco de dados.

* **URL**

  `/books/`


* **Method:**
  
  `GET`

  
*  **URL Params**

   Não há exigência de parâmetros na URL para esta requisição.


* **Success Response:**
  * **Code:** 200 <br />
    **Content:**
    ```json
    {
        "data": [
            {
                "author": "Antoine de Saint-Exupéry",
                "edition": 5,
                "id": 3,
                "isbn": "9788535643411",
                "price": 70.5,
                "publishing_company": "Paulinas",
                "title": "O Pequeno Príncipe - Com Aquarelas do Autor",
                "year": "2020"
            },
            {
                "author": "Alain Mabanckou",
                "edition": 1,
                "id": 4,
                "isbn": "9786588526019",
                "price": 100.0,
                "publishing_company": "Editora Malê",
                "title": "Moisés Negro",
                "year": "2020"
            },
            {
                "author": "Orhan Pamuk",
                "edition": 1,
                "id": 5,
                "isbn": "9788535934076",
                "price": 100.0,
                "publishing_company": "Editora Schwarcz S.A",
                "title": "A Mulher Ruiva",
                "year": "2020"
            }
        ]
    }
    ```
    
* **Sample Call:**

  ```javascript
    var xhr = new XMLHttpRequest();
    xhr.open('GET', 'http://localhost:5000/books/');
    xhr.send();
    xhr.onreadystatechange = () => {
        if(xhr.readyState === 4) console.log(JSON.parse(xhr.responseText));
    }
  ```

**Listar um Livro Específico**
----
  Retorna um JSON contendo um livro específico baseado no id informado no momento da requisição.

* **URL**

    `/books/<int:id>`


* **Method:**
  
  `GET`


*  **URL Params**

   **Required:**
 
   `id=[integer]`


* **Success Response:**

  * **Code:** 200 <br />
    **Content:** 
    ```json
    {
        "data": {
            "author": "Antoine de Saint-Exupéry",
            "edition": 5,
            "id": 3,
            "isbn": "9788535643411",
            "price": 70.5,
            "publishing_company": "Paulinas",
            "title": "O Pequeno Príncipe - Com Aquarelas do Autor",
            "year": "2020"
        }
    }
    ```
    
    OR
    
    ```json
    {
      "error": {
        "message": "Id não encontrado."
      }
    }
    ```
    
* **Sample Call:**

    ```javascript
    var xhr = new XMLHttpRequest();
    xhr.open('GET', 'http://localhost:5000/books/3');
    xhr.send();
    xhr.onreadystatechange = () => {
        if(xhr.readyState === 4) console.log(JSON.parse(xhr.responseText));
    }
  ```
  
**Criar um Novo Livro**
----
  Retorna um JSON com o novo livro cadastrado com os parâmetros informados.

* **URL**

  `/books/`


* **Method:**
  
  `POST`
  

*  **URL Params**

   Não há exigência de parâmetros na URL para esta requisição.



* **Data Params** <br />
    Exemplo JSON de Requisição:
  ```json
    {
        "title": "",
        "author": "",
        "isbn": "",
        "edition": 0,
        "year": "",
        "publishing_company": "",
        "price": 0
    }
  ```
    Dicionário de Dados:
    | # | Field              | Description                | DataType | Required | Unique |
    |:-:|--------------------|----------------------------|:--------:|:--------:|:------:|
    | 1 | title              | Título do Livro            |  String  |   true   |  false |
    | 2 | author             | Autor Principal do Livro   |  String  |   true   |  false |
    | 3 | isbn               | ISBN do Livro              |  String  |   true   |  true  |
    | 4 | edition            | Edição do Livro            |  Integer |   true   |  false |
    | 5 | year               | Ano de Publicação do Livro |  String  |   true   |  false |
    | 6 | publishing_company | Editora do Livro           |  String  |   true   |  false |
    | 7 | price              | Preço do Livro             |   Float  |   true   |  false |
  
* **Success Response:**
  * **Code:** 200 <br />
    **Content:**
    
    ```json
    {
        "data": {
            "author": "Michelle Alexander",
            "edition": 1,
            "id": 2,
            "isbn": "8575595555",
            "price": 49.92,
            "publishing_company": "Boitempo",
            "title": "A nova segregação: racismo e encarceramento em massa",
            "year": "2018"
        }
    }
    ```
    
    OR
    
    ```json
    {
        "errors": [
            {
                "title": "Este campo é obrigatório"
            },
            {
                "author": "Este campo é obrigatório"
            },
            {
                "isbn": "Este campo é obrigatório"
            },
            {
                "edition": "Este campo é obrigatório"
            },
            {
                "year": "Este campo é obrigatório"
            },
            {
                "publishing_company": "Este campo é obrigatório"
            },
            {
                "price": "Este campo é obrigatório"
            }
        ]
    }
    ```

    OR
    
    ```json
    {
        "error": {
            "message": "É esperado um objeto JSON."
        }
    }
    ```

* **Sample Call:**

    ```javascript
    var book = {
        title: 'A nova segregação: racismo e encarceramento em massa',
        author: 'Michelle Alexander',
        isbn: '8575595555',
        edition: 1,
        year: '2018',
        publishing_company: 'Boitempo',
        price: 49.92
    };
  
    var xhr = new XMLHttpRequest();
    xhr.open('POST', 'http://localhost:5000/books/');
    xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    xhr.send(JSON.stringify(book));
    xhr.onreadystatechange = () => {
        if(xhr.readyState === 4) console.log(JSON.parse(xhr.responseText));
    }
  ```  

* **Notes:**

  Há uma validação do número do ISBN, ele aceita o padrão ISBN-10 e ISBN-13. 

**Editar um Livro**
----
  Retorna um JSON com o livro atualizado com os parâmetros informados.

* **URL**

  `/books/<int:id>/`


* **Method:**
  
  `PUT`
  

*  **URL Params**
   
    **Required:**
 
   `id=[integer]`


* **Data Params** <br />
    Exemplo JSON de Requisição:
  ```json
    {
        "title": "",
        "author": "",
        "isbn": "",
        "edition": 0,
        "year": "",
        "publishing_company": "",
        "price": 0
    }
  ```
    Dicionário de Dados:
    | # | Field              | Description                | DataType | Required | Unique |
    |:-:|--------------------|----------------------------|:--------:|:--------:|:------:|
    | 1 | title              | Título do Livro            |  String  |   false  |  false |
    | 2 | author             | Autor Principal do Livro   |  String  |   false  |  false |
    | 3 | isbn               | ISBN do Livro              |  String  |   false  |  true  |
    | 4 | edition            | Edição do Livro            |  Integer |   false  |  false |
    | 5 | year               | Ano de Publicação do Livro |  String  |   false  |  false |
    | 6 | publishing_company | Editora do Livro           |  String  |   false  |  false |
    | 7 | price              | Preço do Livro             |   Float  |   false  |  false |

* **Success Response:**
  * **Code:** 200 <br />
    **Content:**
    
    ```json
    {
        "data": {
            "author": "Antoine de Saint-Exupéry",
            "edition": 5,
            "id": 3,
            "isbn": "1111111111",
            "price": 150.9,
            "publishing_company": "Paulinas",
            "title": "O Pequeno Príncipe - Com Aquarelas do Autor",
            "year": "2020"
        }
    }
    ```
    
    OR
    
    ```json
    {
        "errors": [
            {
                "title": "Este campo é obrigatório"
            },
            {
                "author": "Este campo é obrigatório"
            },
            {
                "isbn": "Este campo é obrigatório"
            },
            {
                "edition": "Este campo é obrigatório"
            },
            {
                "year": "Este campo é obrigatório"
            },
            {
                "publishing_company": "Este campo é obrigatório"
            },
            {
                "price": "Este campo é obrigatório"
            }
        ]
    }
    ```

    OR
    
    ```json
    {
        "error": {
            "message": "É esperado um objeto JSON."
        }
    }
    ```

* **Sample Call:**

    ```javascript
    var bookToUpdate = {
        isbn: '1111111111',
        price: 150.9
    };
  
    var xhr = new XMLHttpRequest();
    xhr.open('PUT', 'http://localhost:5000/books/3');
    xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    xhr.send(JSON.stringify(bookToUpdate));
    xhr.onreadystatechange = () => {
        if(xhr.readyState === 4) console.log(JSON.parse(xhr.responseText));
    }
  ``` 

* **Notes:**

   É necessário submeter apenas os campos que se desejam fazer alterações. Caso um determinado campo seja enviado com _String_ vazia, será retornado uma mensagem de erro dizendo que este campo é obrigatório.


**Excluir um Livro**
----
   É efetuado a exclusão de um livro e retornado um objeto JSON com as dele.

* **URL**

    `/books/<int:id>`


* **Method:**
  
  `DELETE`


*  **URL Params**

   **Required:**
 
   `id=[integer]`


* **Success Response:**

  * **Code:** 200 <br />
    **Content:** 
    ```json
    {
        "data": {
            "author": "Michelle Alexander",
            "edition": 1,
            "id": 1,
            "isbn": "8575595555",
            "price": 49.92,
            "publishing_company": "Boitempo",
            "title": "A nova segregação: racismo e encarceramento em massa",
            "year": "2018"
        },
        "message": "Removido com sucesso."
    }
    ```
    
    OR
    
    ```json
    {
      "error": {
        "message": "Id não encontrado."
      }
    }
    ```
    
* **Sample Call:**

    ```javascript
    var xhr = new XMLHttpRequest();
    xhr.open('DELETE', 'http://localhost:5000/books/1');
    xhr.send();
    xhr.onreadystatechange = () => {
        if(xhr.readyState === 4) console.log(JSON.parse(xhr.responseText));
    }
  ``` 

* **Notes:**

  Quando a requisição é concluída, é retornado o livro que foi excluído, como exemplificado em `Success Response`, mas caso seja efetuada uma consulta pelo id não constará na base de dados. (Não está sendo utilizado deleção lógica).