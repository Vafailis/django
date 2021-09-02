## Install venv
```bash
$ pip install virtulenv
```
## Create venv
```bash
$ python -m venv env
```
## Activate venv
### Windows
```bash
$ env\Scripts\activate
```
### Linux or MacOS
```bash
$ source env/bin/activate
```
## Deactivate venv
### Windows and Linux, MacOS
```bash
$ deactivate
```
## Data Base:
For everything to work correctly, you need to install [PostgreSQL](https://www.postgresql.org/download/)  

## Create tables in DataBase
```bash
$ python manage.py migrate
```
## Populating the DB with data
```bash
$ python manage.py fill_db
```
## Turn on the server
```bash
$ python manage.py runserver
```
## Applications:  
- authapp - application for authorization/registration  
- basketapp - this application describes the operation of the shopping cart in the online store  
- mainapp - store   
