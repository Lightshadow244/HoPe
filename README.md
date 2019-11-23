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
`sudo apt-get install msguniq`  
`sudo apt-get install gettext`  
## Useful comments
Start Server  
`python manage.py runserver 0:8080`  
Manage localization  
`django-admin makemessages -l de`  
`django-admin makemessages -l en`  
`django-admin makemessages -a`  
`django-admin compilemessages`  
