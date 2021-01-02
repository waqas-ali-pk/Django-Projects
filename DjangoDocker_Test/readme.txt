# Dockerize existing django app
# get help from coding for enterpneure blog
# Not completed yet


1. create virtual environment
virtualenv venv

2.
.\venv\Scripts\activate.bat

mkdir src
cd src

## pip3 install django==2.2.4 gunicorn --python 3.6
pip3 install django==2.2.4 gunicorn

django-admin.py startproject DjangoDocker

cd DjangoDocker

python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser

Update Django settings.py
# DEBUG can be True/False or 1/0
DEBUG = int(os.environ.get('DEBUG', default=1)) 

Create .env
DEBUG=1

Test Gunicorn
gunicorn cfehome.wsgi:application --bind 0.0.0.0:8000

Create your Dockerfile
$ cd path/to/your/dev/folder
$ cd simple_dj_docker
$ touch Dockerfile
$ ls
Dockerfile
# Base Image
FROM python:3.6

# create and set working directory
RUN mkdir /app
WORKDIR /app

# Add current directory code to working directory
ADD . /app/

# set default environment variables
ENV PYTHONUNBUFFERED 1
ENV LANG C.UTF-8
ENV DEBIAN_FRONTEND=noninteractive 

# set project environment variables
# grab these via Python's os.environ
# these are 100% optional here
ENV PORT=8000

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
        tzdata \
        python3-setuptools \
        python3-pip \
        python3-dev \
        python3-venv \
        git \
        && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*


# install environment dependencies
RUN pip3 install --upgrade pip 
RUN pip3 install pipenv

# Install project dependencies
RUN pipenv install --skip-lock --system --dev

EXPOSE 8888
CMD gunicorn cfehome.wsgi:application --bind 0.0.0.0:$PORT
