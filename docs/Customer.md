# Módulo de Clientes

Neste arquivo contém a documentação necessária para a utilização das funcionalidades de criação, leitura, edição e deleção de um Cliente.

**Listar Todos os Clientes**
----
Retorna um JSON contendo todos os Clientes cadastrados no banco de dados.

* **URL**

  `/customers/`


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
              "email": "enzocauakaiquerezende_@inpa.gov.br", 
              "first_name": "Enzo", 
              "id": 1, 
              "last_name": " Cauã Kaique Rezende"
            }, 
            {
              "email": "luciaevelynraimundafernandes_@sicredi.com.br", 
              "first_name": "Lúcia", 
              "id": 2, 
              "last_name": "Evelyn Raimunda Fernandes"
            }
          ]
        }
    ```
    
* **Sample Call:**

  ```javascript
    var xhr = new XMLHttpRequest();
    xhr.open('GET', 'http://localhost:5000/customers/');
    xhr.send();
    xhr.onreadystatechange = () => {
        if(xhr.readyState === 4) console.log(JSON.parse(xhr.responseText));
    }
  ```

**Listar um Cliente Específico**
----
  Retorna um JSON contendo um cliente específico baseado no id informado no momento da requisição.

* **URL**

    `/customers/<int:id>`


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
        "email": "luciaevelynraimundafernandes_@sicredi.com.br", 
        "first_name": "Lúcia", 
        "id": 2, 
        "last_name": "Evelyn Raimunda Fernandes"
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
    xhr.open('GET', 'http://localhost:5000/customers/2');
    xhr.send();
    xhr.onreadystatechange = () => {
        if(xhr.readyState === 4) console.log(JSON.parse(xhr.responseText));
    }
  ```
  
**Criar um Novo Cliente**
----
  Retorna um JSON com o novo cliente cadastrado com os parâmetros informados.

* **URL**

  `/customers/`


* **Method:**
  
  `POST`
  

*  **URL Params**

   Não há exigência de parâmetros na URL para esta requisição.



* **Data Params** <br />
    Exemplo JSON de Requisição:
  ```json
    {
        "first_name": "",
        "last_name": "",
        "email": ""
    }
  ```
    Dicionário de Dados:
  | # | Field      | Description          | DataType | Required | Unique |
  |:-:|------------|----------------------|:--------:|:--------:|:------:|
  | 1 | first_name | Nome do Cliente      |  String  |   true   |  false |
  | 2 | last_name  | Sobrenome do Cliente |  String  |   true   |  false |
  | 3 | email      | E-mail do Cliente    |  String  |   true   |  true  |

* **Success Response:**
  * **Code:** 200 <br />
    **Content:**
    
    ```json
    {
        "data": {
            "email": "beatrizveramarciadasilva@arteche.com.br",
            "first_name": "Beatriz",
            "id": 6,
            "last_name": "Vera Márcia da Silva"
        }
    }
    ```
    
    OR
    
    ```json
    {
        "errors": [
            {
                "first_name": "Este campo é obrigatório."
            },
            {
                "last_name": "Este campo é obrigatório."
            },
            {
                "email": "O e-mail informado já encontra-se cadastrado."
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
    var customer = {
        first_name: 'Beatriz',
        last_name: 'Vera Márcia da Silva',
        email: 'beatrizveramarciadasilva@arteche.com.br'
    };
  
    var xhr = new XMLHttpRequest();
    xhr.open('POST', 'http://localhost:5000/customers/');
    xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    xhr.send(JSON.stringify(customer));
    xhr.onreadystatechange = () => {
        if(xhr.readyState === 4) console.log(JSON.parse(xhr.responseText));
    }
  ```  

* **Notes:**

  Há uma validação simples no e-mail com expressão regular, ou seja, é necessário obedecer um padrão de formação não tão complexo. 

**Editar um Cliente**
----
  Retorna um JSON com o cliente atualizado com os parâmetros informados.

* **URL**

  `/customers/<int:id>/`


* **Method:**
  
  `PUT`
  

*  **URL Params**
   
    **Required:**
 
   `id=[integer]`


* **Data Params** <br />
    Exemplo JSON de Requisição:
  ```json
    {
        "first_name": "",
        "last_name": "",
        "email": ""
    }
  ```
    Dicionário de Dados:
  | # | Field      | Description          | DataType | Required | Unique |
  |:-:|------------|----------------------|:--------:|:--------:|:------:|
  | 1 | first_name | Nome do Cliente      |  String  |   false  |  false |
  | 2 | last_name  | Sobrenome do Cliente |  String  |   false  |  false |
  | 3 | email      | E-mail do Cliente    |  String  |   false  |  true  |

* **Success Response:**
  * **Code:** 200 <br />
    **Content:**
    
    ```json
    {
        "data": {
            "email": "beatrizveramarciadasilva@gmail.com",
            "first_name": "Beatriz",
            "id": 6,
            "last_name": "Vera Márcia da Silva"
        }
    }
    ```
    
    OR
    
    ```json
    {
        "errors": [
            {
                "first_name": "Este campo é obrigatório."
            },
            {
                "last_name": "Este campo é obrigatório."
            },
            {
                "email": "O e-mail informado já encontra-se cadastrado."
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
    var customerToUpdate = {
        email: 'beatrizveramarciadasilva@gmail.com.br'
    };
  
    var xhr = new XMLHttpRequest();
    xhr.open('PUT', 'http://localhost:5000/customers/6');
    xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    xhr.send(JSON.stringify(customerToUpdate));
    xhr.onreadystatechange = () => {
        if(xhr.readyState === 4) console.log(JSON.parse(xhr.responseText));
    }
  ``` 

* **Notes:**

   É necessário submeter apenas os campos que se desejam fazer alterações. Caso um determinado campo seja enviado com _String_ vazia, será retornado uma mensagem de erro dizendo que este campo é obrigatório.


**Excluir um Cliente**
----
  É efetuado a exclusão de um cliente e retornado um objeto JSON com as dele.

* **URL**

    `/customers/<int:id>`


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
            "email": "luciaevelynraimundafernandes_@sicredi.com.br",
            "first_name": "Lúcia",
            "id": 2,
            "last_name": "Evelyn Raimunda Fernandes"
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
    xhr.open('DELETE', 'http://localhost:5000/customers/2');
    xhr.send();
    xhr.onreadystatechange = () => {
        if(xhr.readyState === 4) console.log(JSON.parse(xhr.responseText));
    }
  ``` 

* **Notes:**

  Quando a requisição é concluída, é retornado o cliente que foi excluído, como exemplificado em `Success Response`, mas caso seja efetuada uma consulta pelo id não constará na base de dados. (Não está sendo utilizado deleção lógica).