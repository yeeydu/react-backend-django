## install python to your machine
project in another folder

python project installation commands

- python3 -m venv .venv
- . .venv/bin/activate

Install Django 
- python -m pip install django
- django-admin
- django-admin startptoject "name" .

Run server
- python3 manage.py runserver

For any installation use pip

- pip install name

to see all installed packages
- pip freeze

file to keep track of all packages you install
- pip freeze > requirements.txt
install al packages for the project like (npm install)
- pip install -r requirements.txt

migration
- python manage.py migrate
new migration
- python manage.py makemigrations "name"
- python manage.py migrate

Admin
- python manage.py createsuperuser

CORS
- pip install django-cors-headers
