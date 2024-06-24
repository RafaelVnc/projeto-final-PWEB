# PROJETO FINAL PWEB
Final Web Programming discipline project from the course of Analysis and Systems Development at [Centro Universitário de Brasília](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwi634e6mc-FAxUpDbkGHQU9A3YQFnoECAcQAQ&url=https%3A%2F%2Fwww.uniceub.br%2F&usg=AOvVaw0TbSk6nDGc08eChcMUv3_w&opi=89978449).

## Skills

**FastAPI, PostgreSQL, Async SQLAlchemy, Uvicorn, HTML, CSS**

## Functionalities
* Add User
* Add Favorite Active for an User
* Delete User
* Delete Favorite Active
* List Users and their respective Favorite Actives

## Dependecies
* Docker
* Docker-compse
* Python >= 3.11
* Poetry

## How to run
Add project path at PYTHONPATH variable in .env file.

Start **postgres** database and **pgadmin**
```shell
docker-compose up -d
```

Start environment
```shell
poetry shell
```

Install python dependencies
```shell
poetry install
```

init database
```shell
python database\init_db.py
```

Start application
```shell
uvicorn app.main:app --port 8080
```
More documentation in /docs.

## Authors
### Rafael Oliveira Venancio  
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/rafael-oliveira-venancio-6904122a6/)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/RafaelVnc)
### Wesley Oliveira
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/wesley-ricardo-oliveira-da-silva-748443269?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app)
