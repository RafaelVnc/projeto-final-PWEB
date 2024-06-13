# PROJETO FINAL PWEB
Projeto final da disciplina de Programação Web do curso de Análise e desenvolvimento de sistemas do [Centro Universitário de Brasília](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwi634e6mc-FAxUpDbkGHQU9A3YQFnoECAcQAQ&url=https%3A%2F%2Fwww.uniceub.br%2F&usg=AOvVaw0TbSk6nDGc08eChcMUv3_w&opi=89978449).

## Skills

**FastAPI, PostgreSQL, Async SQLAlchemy, Uvicorn, HTML, CSS**

## Funcionalidades
* Adicionar usuário
* Adicionar ativo favorito para um usuário
* Deletar usuário
* Deletar ativo favorito de um usuário
* Listar usuários e seus ativos favoritos

## Dependências
* Docker
* Docker-compse
* Python >= 3.11
* Poetry

## Como rodar

Inicie banco de dados **postgres** e **pgadmin**
```shell
docker-compose up -d
```

Inicie o ambiente
```shell
poetry shell
```

Instale as dependências do python
```shell
poetry install
```

Instâncie o banco de dados
```shell
python database\init_db.py
```

Inicie a aplicação
```shell
uvicorn app.main:app --port 8080
```
Mais documentação em /docs.

## Autores
### Rafael Oliveira Venancio  
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/rafael-oliveira-venancio-6904122a6/)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/RafaelVnc)
### Wesley Oliveira
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/wesley-ricardo-oliveira-da-silva-748443269?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app)
