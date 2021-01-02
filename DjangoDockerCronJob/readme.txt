# Create django project on docker and setup cronjob

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

RUN apt-get update
RUN apt-get install nano

RUN apt-get install -y cron

RUN python manage.py crontab add
RUN python manage.py crontab show

##########

create requirements.txt file
Django==2.2
python-crontab==2.5.1

Docker-compose file content:
version: '3'

services:
  web:
    build: .
    command: python manage.py runserver 0.0.0.0:8000
    volumes:
     - .:/app
    ports:
     - "8000:8000"
#######

docker-compose run web django-admin.py startproject dockerprojectcronjob .

ls -l ## command not working in windows vs code terminal

docker-compose run web django-admin.py startapp dockerappcronjob

docker-compose up

Additional steps: (additional steps are performed as new packages added in requirements.txt file)
requirements.txt file updated.
add following apps in settings.py file (under INSTALLED_APPS):
  'dockerappcronjob',
  'django_crontab',
rebuild docker-compose:
  docker-compose build
run docker again:
  docker-compose up


# open new terminal and run following command to start cron service on docker
docker exec -it djangodockercronjob_web_1 cron

########################
Help:
docker ps to list running containers and locate the one
docker exec -it [container_name] bash to login to the bash shell on that container
cd to the django project and run python manage.py [command]
########################
