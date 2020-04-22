# HoPe
A website  
## Requirements
- virtualenv with python 3
- django
### example
`sudo apt-get update && upgrade`
`sudo apt-get install python3`  
`sudo apt-get install python3-pip`  
`python3 -m pip install virtualenv`  
`virtualenv -p /usr/bin/python3 ENV`  
`source ENV/bin/activate`  
`pip install django`  
Manage localization  
`sudo apt-get install gettext`  
uswgi setup  
https://uwsgi-docs.readthedocs.io/en/latest/tutorials/Django_and_nginx.html  
Start uwsgi server  
`uwsgi --socket HoPe.sock --module HoPe.wsgi --chmod-socket=666 --logto ~/logs/HoPe.log &`
## Useful comments
inital DB  
`python manage.py makemigrations Foerder`  
`python manage.py migrate`  
Start Server  
`python manage.py runserver 0:8080`  
Manage localization  
`django-admin makemessages -l de`  
`django-admin makemessages -l en`  
`django-admin makemessages -a`  
`django-admin compilemessages`  
Collect static files  
`python manage.py collectstatic`
