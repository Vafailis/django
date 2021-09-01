## For start my django project  
```bash
$ pip install virtualenv
$ python -m venv env
$ env\Scripts\activate
$ cd project
$ pip install -r requirements.txt
$ cd stepshop
$ python manage.py migrate
$ python manage.py fill_db
$ python manage.py runserver
```
## Applications:  
- authapp - application for authorization/registration  
- basketapp - this application describes the operation of the shopping cart in the online store  
- mainapp - store   
## Data Base:
For everything to work correctly, you need to install [PostgreSQL](https://www.postgresql.org/download/)
