from __future__ import absolute_import, unicode_literals # for python2

import os
from celery import Celery
from celery.schedules import crontab

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dockerceleryproject.settings')

# Get the base REDIS URL, default to redis' default
BASE_REDIS_URL = os.environ.get('REDIS_URL', 'redis://localhost:6379')

app = Celery('dockerceleryproject')

# Using a string here means the worker don't have to serialize
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

app.conf.broker_url = BASE_REDIS_URL

# this allows you to schedule items in the Django admin.
app.conf.beat_scheduler = 'django_celery_beat.schedulers.DatabaseScheduler'

# Schedule tasks here - celery beat
app.conf.beat_schedule = {
    'email-every-5-sec': {
        'task': 'send_email',
        'schedule': 5.0,
        'args': ('jobs', 'jobs@apple.com')
    },
}
