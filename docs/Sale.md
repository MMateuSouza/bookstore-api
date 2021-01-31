# Módulo de Vendas

Neste arquivo contém a documentação necessária para a utilização das funcionalidades de criação e leitura das Vendas.

**Listar Todas as Vendas**
----
Retorna um JSON contendo todas as Vendas cadastradas no banco de dados.

* **URL**

  `/sales/`


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
                "customer_id": 3,
                "discount": 0.0,
                "grand_total": 550.9,
                "id": 1,
                "purchase_date": "Sun, 31 Jan 2021 19:49:43 GMT",
                "shopping_cart": [
                    {
                        "book": {
                            "author": "Antoine de Saint-Exupéry",
                            "edition": 5,
                            "id": 3,
                            "isbn": "1111111111",
                            "price": 150.9,
                            "publishing_company": "Paulinas",
                            "title": "O Pequeno Príncipe - Com Aquarelas do Autor",
                            "year": "2020"
                        },
                        "book_id": 3,
                        "id": 1,
                        "quantity": 1,
                        "sale_id": 1
                    },
                    {
                        "book": {
                            "author": "Alain Mabanckou",
                            "edition": 1,
                            "id": 4,
                            "isbn": "9786588526019",
                            "price": 100.0,
                            "publishing_company": "Editora Malê",
                            "title": "Moisés Negro",
                            "year": "2020"
                        },
                        "book_id": 4,
                        "id": 2,
                        "quantity": 1,
                        "sale_id": 1
                    },
                    {
                        "book": {
                            "author": "Orhan Pamuk",
                            "edition": 1,
                            "id": 5,
                            "isbn": "9788535934076",
                            "price": 100.0,
                            "publishing_company": "Editora Schwarcz S.A",
                            "title": "A Mulher Ruiva",
                            "year": "2020"
                        },
                        "book_id": 5,
                        "id": 3,
                        "quantity": 1,
                        "sale_id": 1
                    },
                    {
                        "book": {
                            "author": "Antonio Skármeta",
                            "edition": 1,
                            "id": 6,
                            "isbn": "9786555870985",
                            "price": 100.0,
                            "publishing_company": "Editora Record LTDA",
                            "title": "Um Dia em Que a Poesia Derroutou um Ditador",
                            "year": "2020"
                        },
                        "book_id": 6,
                        "id": 4,
                        "quantity": 2,
                        "sale_id": 1
                    }
                ],
                "subtotal": 550.9
            },
            {
                "customer_id": 6,
                "discount": 0.0,
                "grand_total": 439.92,
                "id": 2,
                "purchase_date": "Sun, 31 Jan 2021 19:50:06 GMT",
                "shopping_cart": [
                    {
                        "book": {
                            "author": "J.K. Rowling",
                            "edition": 1,
                            "id": 10,
                            "isbn": "9788532529954",
                            "price": 100.0,
                            "publishing_company": "Editora Rocco LTDA",
                            "title": "Harry Potter e a Pedra Filosofal",
                            "year": "2015"
                        },
                        "book_id": 10,
                        "id": 5,
                        "quantity": 1,
                        "sale_id": 2
                    },
                    {
                        "book": {
                            "author": "J.K. Rowling",
                            "edition": 1,
                            "id": 12,
                            "isbn": "9788532529978",
                            "price": 100.0,
                            "publishing_company": "Editora Rocco LTDA",
                            "title": "Harry Potter e o Prisioneiro de Azkaban",
                            "year": "2015"
                        },
                        "book_id": 12,
                        "id": 6,
                        "quantity": 1,
                        "sale_id": 2
                    },
                    {
                        "book": {
                            "author": "J.K. Rowling",
                            "edition": 1,
                            "id": 14,
                            "isbn": "9788532530004",
                            "price": 100.0,
                            "publishing_company": "Editora Rocco LTDA",
                            "title": "Harry Potter e o Enigma do Príncipe",
                            "year": "2015"
                        },
                        "book_id": 14,
                        "id": 7,
                        "quantity": 1,
                        "sale_id": 2
                    },
                    {
                        "book": {
                            "author": "J.K. Rowling",
                            "edition": 1,
                            "id": 16,
                            "isbn": "9788532529992",
                            "price": 100.0,
                            "publishing_company": "Editora Rocco LTDA",
                            "title": "Harry Potter e a Ordem da Fênix",
                            "year": "2015"
                        },
                        "book_id": 16,
                        "id": 8,
                        "quantity": 1,
                        "sale_id": 2
                    },
                    {
                        "book": {
                            "author": "David Epstein",
                            "edition": 1,
                            "id": 18,
                            "isbn": "9786580634347",
                            "price": 39.92,
                            "publishing_company": "Globo Livros",
                            "title": "Por que os generalistas vencem em um mundo de especialistas",
                            "year": "2020"
                        },
                        "book_id": 18,
                        "id": 9,
                        "quantity": 1,
                        "sale_id": 2
                    }
                ],
                "subtotal": 439.92
            }
        ]
    }
    ```
    
* **Sample Call:**

  ```javascript
    var xhr = new XMLHttpRequest();
    xhr.open('GET', 'http://localhost:5000/sales/');
    xhr.send();
    xhr.onreadystatechange = () => {
        if(xhr.readyState === 4) console.log(JSON.parse(xhr.responseText));
    }
  ```

**Listar uma Venda Específica**
----
  Retorna um JSON contendo uma venda específica baseada no id informado no momento da requisição.

* **URL**

    `/sales/<int:id>`


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
            "customer_id": 6,
            "discount": 0.0,
            "grand_total": 439.92,
            "id": 2,
            "purchase_date": "Sun, 31 Jan 2021 19:50:06 GMT",
            "shopping_cart": [
                {
                    "book": {
                        "author": "J.K. Rowling",
                        "edition": 1,
                        "id": 10,
                        "isbn": "9788532529954",
                        "price": 100.0,
                        "publishing_company": "Editora Rocco LTDA",
                        "title": "Harry Potter e a Pedra Filosofal",
                        "year": "2015"
                    },
                    "book_id": 10,
                    "id": 5,
                    "quantity": 1,
                    "sale_id": 2
                },
                {
                    "book": {
                        "author": "J.K. Rowling",
                        "edition": 1,
                        "id": 12,
                        "isbn": "9788532529978",
                        "price": 100.0,
                        "publishing_company": "Editora Rocco LTDA",
                        "title": "Harry Potter e o Prisioneiro de Azkaban",
                        "year": "2015"
                    },
                    "book_id": 12,
                    "id": 6,
                    "quantity": 1,
                    "sale_id": 2
                },
                {
                    "book": {
                        "author": "J.K. Rowling",
                        "edition": 1,
                        "id": 14,
                        "isbn": "9788532530004",
                        "price": 100.0,
                        "publishing_company": "Editora Rocco LTDA",
                        "title": "Harry Potter e o Enigma do Príncipe",
                        "year": "2015"
                    },
                    "book_id": 14,
                    "id": 7,
                    "quantity": 1,
                    "sale_id": 2
                },
                {
                    "book": {
                        "author": "J.K. Rowling",
                        "edition": 1,
                        "id": 16,
                        "isbn": "9788532529992",
                        "price": 100.0,
                        "publishing_company": "Editora Rocco LTDA",
                        "title": "Harry Potter e a Ordem da Fênix",
                        "year": "2015"
                    },
                    "book_id": 16,
                    "id": 8,
                    "quantity": 1,
                    "sale_id": 2
                },
                {
                    "book": {
                        "author": "David Epstein",
                        "edition": 1,
                        "id": 18,
                        "isbn": "9786580634347",
                        "price": 39.92,
                        "publishing_company": "Globo Livros",
                        "title": "Por que os generalistas vencem em um mundo de especialistas",
                        "year": "2020"
                    },
                    "book_id": 18,
                    "id": 9,
                    "quantity": 1,
                    "sale_id": 2
                }
            ],
            "subtotal": 439.92
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
    xhr.open('GET', 'http://localhost:5000/sales/2');
    xhr.send();
    xhr.onreadystatechange = () => {
        if(xhr.readyState === 4) console.log(JSON.parse(xhr.responseText));
    }
  ```
  
**Criar uma Venda**
----
  Retorna um JSON com a nova venda cadastrada com os parâmetros informados.

* **URL**

  `/sales/`


* **Method:**
  
  `POST`
  

*  **URL Params**

   Não há exigência de parâmetros na URL para esta requisição.


* **Data Params** <br />
    Exemplo JSON de Requisição:
  ```json
    {
        "customer_id": 0,
        "books_ids": []
    }
  ```
    Dicionário de Dados:
    | # | Field       | Description                                                            |    DataType    | Required | Unique |
    |:-:|-------------|------------------------------------------------------------------------|:--------------:|:--------:|:------:|
    | 1 | customer_id | Id do Cliente que Realizou a Compra                                    |     Integer    |   true   |  false |
    | 2 | books_ids   | Lista de Números Inteiros que Representam os Ids dos Livros Comprados. | Array(Integer) |   true   |  false |
  
* **Success Response:**
  * **Code:** 200 <br />
    **Content:**
    
    ```json
    {
        "data": {
            "customer_id": 6,
            "discount": 0.0,
            "grand_total": 452.70000000000005,
            "id": 4,
            "purchase_date": "Sun, 31 Jan 2021 19:58:43 GMT",
            "shopping_cart": [
                {
                    "book": {
                        "author": "Antoine de Saint-Exupéry",
                        "edition": 5,
                        "id": 3,
                        "isbn": "1111111111",
                        "price": 150.9,
                        "publishing_company": "Paulinas",
                        "title": "O Pequeno Príncipe - Com Aquarelas do Autor",
                        "year": "2020"
                    },
                    "book_id": 3,
                    "id": 11,
                    "quantity": 3,
                    "sale_id": 4
                }
            ],
            "subtotal": 452.70000000000005
        }
    }
    ```
    
    OR
    
    ```json
    {
        "errors": [
            {
                "customer_id": "Este campo é obrigatório."
            },
            {
                "books_ids": "Este campo é obrigatório e/ou é esperado uma lista de inteiros. Ela não pode estar vazia. Ex.: [1, 2, ..., 10]"
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
    var sale = {
        customer_id: 6,
        books_ids: [3, 3, 3]
    };
  
    var xhr = new XMLHttpRequest();
    xhr.open('POST', 'http://localhost:5000/sales/');
    xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    xhr.send(JSON.stringify(sale));
    xhr.onreadystatechange = () => {
        if(xhr.readyState === 4) console.log(JSON.parse(xhr.responseText));
    }
  ```  

* **Notes:**

  Em `Sample Call` é possível notar que `sales.books_ids` é uma lista contendo três números repetidos, isso é uma regra de negócio aplicada, ou seja, isso representa que o cliente efetuou a compra de três livros com aquele `id`.

  Há uma regra de negócio que especifica a quantidade máxima de Livros distintos por compra (`n = 10`), ou seja, supondo que eu tenho livros com os `ids` de 1 até 10, esta lista `[1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]` representa que comprei três livros com o `id=1` e um livro de cada dos outros `ids`.

  Além dos campos ilustrados no Dicionário de Dados em `Data Params`, a venda possui alguns campos que são gerados, segue abaixo:

    | # | Field         | Description                                                                                                             | DataType | Required | Unique |
    |:-:|---------------|-------------------------------------------------------------------------------------------------------------------------|:--------:|:--------:|:------:|
    | 1 | subtotal      | O valor final da Compra                                                                                                 |   Float  |   false  |  false |
    | 2 | discount      | O valor do desconto baseado no histórico de Compras do Cliente. (Regra de negócio especificada na proposta do projeto). |   Float  |   false  |  false |
    | 3 | grand_total   | O valor final da Compra, ou seja, o subtotal com o desconto aplicado.                                                   |   Float  |   false  |  false |
    | 4 | purchase_date | A data e hora de quando foi efetuado o registro da Compra                                                               | DateTime |   false  |  false |
