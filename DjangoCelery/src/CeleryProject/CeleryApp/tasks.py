import random
from celery import shared_task
# from celery.task import PeriodTask
# from celery.schedules import crontab
# from datetime import timedelta


@shared_task(name="email_digest_task")
def email_digest(name, email):
    print(f"Digest sent to {name} at {email}")


@shared_task(name="send_email_task")
def send_email(name, email):
    print(f"Email sent to {name} at {email}")

# @shared_task
# def addreport(x, y):
#     print("Celery add_report function started.")
#     return x + y

# class MyCustomSchedularTask(PeriodTask):
#     run_every = crontab(minute=1) #  timedelta(minutes=1) #  

#     def run(self, **kwargs):
#         print("Adding task from custom schedular. PeriodTask.")
#         addreport(500, 600)
