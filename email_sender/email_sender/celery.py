from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'email_sender.settings')
django.setup()

app = Celery("email_sender")
app.conf.enable_utc = False
app.conf.update(timezone='Europe/Amsterdam')

app.config_from_object("django.conf:settings", namespace="CELERY")

app.conf.beat_schedule = {
    'Send_mail_to_Client': {
        'task': 'email_send.tasks.send_emails_schedule',
        'schedule': 120
    }
}
app.autodiscover_tasks()
