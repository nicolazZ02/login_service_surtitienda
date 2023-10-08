# FastAPI MicroServie Clean Architecture

Using FastAPI - Microservices.

Integration with FastAPI, pydantic, SQLAlchemy extensions and others.

### REQUIRED!:

All libraries esecificated in pyproject.tomls

Install in your ide SonarLint extension

- Python3.9

Requirements libs:

- python = "^3.9"
- fastapi = "^0.95.1"
- python-dotenv = "^1.0.0"
- sqlacodegen = "^2.3.0.post1"
- psycopg2 = "^2.9.6"
- uvicorn = {extras = ["standard"], version = "^0.22.0"}
- pydantic = {extras = ["email"], version = "^1.10.7"}
- orjson = "^3.8.12"
- asyncpg = "^0.27.0"

### Extension:

- FastAPI: [FastAPI](https://fastapi.tiangolo.com/)

- SQL ORM: [SQLAlchemy](https://www.sqlalchemy.org/)

- Testing: [pytest](https://docs.pytest.org/en/latest/)

## Installation

Install with pip3:



$ cd ProjectFolder
$ python3 -m venv venv
$ . venv/bin/activate
$ cp .env.example .env -> #Edit .env file
$ pip3 install poetry
$ poetry install
$ poetry run uvicorn app.main:app --reload



## FastAPI Application Structure 

.
|──────app/
| |────common/
| |────controller/
| |────models/
| |────repository/
| |────service/
| |────__init__.py
| |────main.py
|──────logs/
| |────app.log
|──────test/
|──────.env
|──────.env.exmaple
|──────.gitignore
|──────dockerfile
|──────generateModel.bat
|──────gunicorn_conf.py
|──────Makefile
|──────pyproject.toml
|──────README.md

|──────app/
|──────Logs/
|──────test/




## FastAPI Configuration

#### Example 

common/helper/constantsHelper.py

python

MY_CONSTANT = "my_constant"



#### Builtin Configuration Values 

edit .env file with base64 encode
ignore base64 encode in BACKEND_CORS_ORIGINS

python

DATABASE_SERVER="bG9jYWxob3N0"
DATABASE_NAME="YmFzZS1weXRob24="
DATABASE_USER="cG9zdGdyZXM="
DATABASE_PASSWORD="bW9rMTAwMDY="
DATABASE_PORT="NTQzMg=="
SECRET_KEY="MmYwMDEwMjQ3M2ZlNmFkMjBmZDM1YzQxODVlN2ZkMDllNGVjM2Q4ZTIyOTdmZTY2"
BACKEND_CORS_ORIGINS=["http://localhost"]


 
## Run FastAPI
### Run flask for develop

$ poetry run uvicorn app.main:app --reload


### Run fastapi for debug

Use integrated debug in your IDE with the following configuration file:

Visual Studio Code Example

```
{
    // Use IntelliSense to learn about possible attributes.
    // Hover to view descriptions of existing attributes.
    // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: FastAPI",
            "type": "python",
            "request": "launch",
            "module": "uvicorn",
            "args": [
                "app.main:app"
            ],
            "jinja": true,
            "justMyCode": true
        }
    ]
}
```

### Run fastapi for production


$ poetry run gunicorn app.main:app --config gunicorn_conf.py



In FastAPI, Default port is `8000`

Swagger document page:  `http://127.0.0.1:8000/docs`

## Reference

Offical Website

- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [pytest](https://docs.pytest.org/en/latest/)

## Changelog

- Author: [Juan Sebastian Leon Henao](mailto:juan.leon@grupomok.com)
- Author: [Nicolas Andres Gomez Leal](mailto:nicolasandresgomez1999@gmail.com)
- Author: [Richard Alberto Ramirez Ruiz](mailto:richardramirez1709@gmail.com)
- Position: Desarrolladores Junior
- Date: 2023-08-23
- Version 1.0.0 : First document guide
- Version 1.1.0 : Upgrade required python version to 3.9