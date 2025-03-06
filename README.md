# Meu Projeto de Testes de API

Este projeto contém scripts de teste em Python utilizando a biblioteca `requests` para testar a API pública `https://jsonplaceholder.typicode.com/posts`.

## Estrutura do Projeto

```
meu_projeto/
│── modules/
│   ├── __init__.py
│   ├── api_config.py
│   ├── module_post_test.py
│── tests/
│   ├── test_example.py
│── main.py
│── README.md
```

## Pré-requisitos

- Python 3.x
- Biblioteca `requests`

## Instalação

1. Clone o repositório para o seu ambiente local:
    ```sh
    git clone <URL_DO_REPOSITORIO>
    cd meu_projeto
    ```

2. Crie um ambiente virtual:
    ```sh
    python -m venv venv
    ```

3. Ative o ambiente virtual:

    - No Windows:
        ```sh
        venv\Scripts\activate
        ```
    - No macOS/Linux:
        ```sh
        source venv/bin/activate
        ```

4. Instale as dependências:
    ```sh
    pip install requests
    ```

## Executando os Testes

Para executar os testes, utilize o script `main.py`:

```sh
python main.py
```

## Descrição dos Testes

- `test_get_posts`: Realiza uma requisição GET para a API e valida a resposta.
- `test_create_post`: Realiza uma requisição POST para a API com dados aleatórios e valida a resposta.

As respostas das requisições GET, POST e DELETE serão impressas na tela.

## Contato

Para mais informações, entre em contato com [seu_email@dominio.com].