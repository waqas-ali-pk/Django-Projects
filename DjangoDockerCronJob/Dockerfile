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
