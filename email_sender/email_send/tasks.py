from celery import shared_task, Celery
from django.conf import settings

from sender import send_emails_to_users
app = Celery('tasks', broker="redis://localhost:6379/0")


@shared_task()
def send_emails_schedule():
    content = {'template': 'email.html', 'subject': 'Promo Email'}
    send_emails_to_users(content)

