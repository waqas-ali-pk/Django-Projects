from __future__ import absolute_import, unicode_literals # for python2

import os
from celery import Celery
from celery.schedules import crontab

# set the default Django settings module for the 'celery' program.
# this is also used in manage.py
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CeleryProject.settings')


# Get the base REDIS URL, default to redis' default
BASE_REDIS_URL = os.environ.get('REDIS_URL', 'redis://localhost:6379')

app = Celery('CeleryProject')

# Using a string here means the worker don't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

app.conf.broker_url = BASE_REDIS_URL

# this allows you to schedule items in the Django admin.
app.conf.beat_scheduler = 'django_celery_beat.schedulers.DatabaseScheduler'

# Schedule tasks here - celery beat
app.conf.beat_schedule = {
    'email-digest-contrab': {
        'task': 'send_email_task',
        'schedule': crontab(hour=5, minute=30, day_of_week=1),
        'args': ('larry', 'larry@google.com'),
    },
    'email-every-5-sec': {
        'task': 'send_email_task',
        'schedule': 5.0,
        'args': ('steve', 'steve@apple.com')
    },
    'email-every-30-sec': {
        'task': 'email_digest_task',
        'schedule': 30.0,
        'args': ('bill', 'bill@microsoft.com')
    },
}
