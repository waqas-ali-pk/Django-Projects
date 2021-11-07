# Create django project on docker

1. create docker compose
docker-compose.yml

create docker file.
Dockerfile

#####
Docker file content:

FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /app
WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY . /app/

##########

create requirements.txt file
Django==2.2
celery==4.4.7
redis==3.5.3
django-celery-beat==1.5.0
django-celery-results==1.1.2

Docker-compose file content:
version: '3'

services:
  web:
    build: .
    command: bash -c "python manage.py makemigrations
            && python manage.py migrate
            && python manage.py runserver 0.0.0.0:8000
            "
    volumes:
     - .:/app
    ports:
     - "8000:8000"
    depends_on: 
      - redis
  redis:
    image: "redis:alpine"
  worker_1:
    build: .
    hostname: worker_1
    command: celery -A dockerceleryproject worker -l info --max-tasks-per-child=1
    volumes:
      - .:/app
    depends_on: 
      - redis
  worker_2:
    build: .
    hostname: worker_2
    command: celery -A dockerceleryproject worker -l info --max-tasks-per-child=1
    volumes:
      - .:/app
    depends_on: 
      - redis
  beat:
    build: .
    command: celery -A dockerceleryproject beat -l info
    volumes:
      - .:/app
    depends_on: 
      - redis

#######

docker-compose run web django-admin.py startproject dockerceleryproject .

ls -l ## command not working in windows vs code terminal

docker-compose run web django-admin.py startapp dockerceleryapp


##############

# Add following apps in INSTALLED_APPS in settings.py:
    'dockerceleryapp',
    'django_celery_beat',
    'django_celery_results',

Add following line in settings.py file:
CELERY_RESULT_BACKEND = "django-db"

Navigate to root project config module (where settings and urls modules are)
Create a celery.py file with the contents:

<CHECK FILE FOR CONTENT>

Update project configuration folder's __init__.py file:
It's the __init__.py located in the same directory as settings.py

<CHECK FILE FOR CONTENT>

create tasks.py file in dockerceleryapp with following content:

<CHECK FILE FOR CONTENT>

Add following lines in settings.py file
CELERY_BROKER_URL = 'redis://redis:6379'
CELERY_RESULT_BACKEND = 'redis://redis:6379'

# build docker
docker-compose build

# run docker
docker-compose up

#### docker exec -it container_id python manage.py createsuperuser

# create super user
docker-compose run web /app/manage.py createsuperuser

#####
# See logs of celery worker/beat inside docker.
sudo docker logs -f "Image_name_of_celery"

Note: "Image_name_of_celery" => check with docker image name or container id.

# Check all the running docker containers and images
sudo docker ps

#####################
For standalone worker
create new folder (standalone_worker) and create new docker-compose file

Content of new docker-compose file.

version: '3'

services:
  worker_3:
    build: .
    hostname: worker_3
    command: celery -A dockerceleryproject worker -l info --max-tasks-per-child=1
    volumes:
      - .:/app
    networks: 
      - worker-net

networks: 
  worker-net:
    external: 
      name: redis-network-ext


Copy required project files inside standalone_worker folder 
# need to check, how this can be improved. (without copying code in this folder)

#####################

network details added in both docker-compose files, for cross docker communication.      


