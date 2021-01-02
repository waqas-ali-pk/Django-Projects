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

docker-compose run web django-admin.py startproject dockerproject .

ls -l ## command not working in windows vs code terminal

docker-compose run web django-admin.py startapp dockerapp

docker-compose up








