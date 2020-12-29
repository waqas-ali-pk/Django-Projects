#create virtual environment.
virtualenv venv

# activate virtual env
.\venv\Scripts\activate

mkdir src && cd src

# install django
pip install django==2.2

django-admin startproject CeleryProject

cd CeleryProject

manage.py startapp CeleryApp

pip freeze > requirements.txt

python manage.py migrate
python manage.py createsuperuser

# user: waqas.ali
# pass: waqas.ali

#######

# Install Celery & Redis Python Packages
pip install celery==4.4.7
pip install redis
pip install django-celery-beat
pip install django-celery-results

# open project in visual studio code
code .

# Update Django settings.py:
INSTALLED_APPS += [
    'django_celery_beat',
    'django_celery_results',
]

CELERY_RESULT_BACKEND = "django-db"

python manage.py makemigrations
python manage.py migrate

Navigate to root project config module (where settings and urls modules are)
Create a celery.py file with the contents:

<CONTENT>

Update project configuration folder's __init__.py file:
It's the __init__.py located in the same directory as settings.py

Create tasks.py in any Django app (a valid app in INSTALLED_APPS):

Test tasks:
Open a terminal window, and run a celery worker with in your project root (where manage.py lives).

celery -A CeleryProject worker -l info

For Windows:
It worked for me:
celery -A CeleryProject worker --pool=solo -l info
basically things become single threaded and are suppoted

## second worker
celery -A CeleryProject worker -n worker2 --pool=solo -l info

Setup Schedule to Run Tasks:

Run Scheduled Tasks With Celery Beat:
Open another Terminal window to run scheduled tasks:
celery -A CeleryProject worker --beat -l info -S django
-S django tells celery to use the Django database scheduler.
You can also have the beat server run as it's own process with 
celery -A CeleryProject beat -l info


# celery flower
Installation
Installing flower with pip is simple

$ pip install flower
Development version can be installed with

$ pip install https://github.com/mher/flower/zipball/master#egg=flower
Usage
Launch the server and open http://localhost:5555

$ flower -A proj --port=5555
Or, launch from Celery

$ celery flower -A proj --address=127.0.0.1 --port=5555
Broker URL and other configuration options can be passed through the standard Celery options

$ celery flower -A proj --broker=amqp://guest:guest@localhost:5672//

#### command to run flower
celery flower -A CeleryProject --broker=redis://localhost:6379//

#-- 1
celery -A CeleryProject flower --broker=redis://localhost:6379//

#-- 2
celery -A CeleryProject flower

celery events: Curses Monitor
celery -A CeleryProject events
