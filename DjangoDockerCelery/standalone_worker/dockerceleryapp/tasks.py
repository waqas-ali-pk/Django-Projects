import random
import time
from celery import shared_task


@shared_task(name="send_email")
def send_email(name, email):
    print("Email sending started")
    time.sleep(7)
    print(f"Email sent to {name} at {email}")
