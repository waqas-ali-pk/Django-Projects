import random
from celery import shared_task
from celery.task import PeriodicTask
from celery.schedules import crontab
# from datetime import timedelta


@shared_task(name="email_digest_task")
def email_digest(name, email):
    print(f"Digest sent to {name} at {email}")


@shared_task(name="send_email_task")
def send_email(name, email):
    print(f"Email sent to {name} at {email}")


@shared_task
def generate_report(name):
    print(f"{name} report generated successfully.")


class GenerateReportHourly(PeriodicTask):
    run_every = crontab(hour='*/1')  # timedelta(minutes=1)

    def run(self, **kwargs):
        print("Adding task from class based periodic scheduler.")
        generate_report("John")
