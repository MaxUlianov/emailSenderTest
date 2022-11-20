from django.core.mail import send_mail
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'email_sender.settings')
django.setup()

from email_send.models import User
from django.template.loader import render_to_string
from django.utils.html import strip_tags


def send_email(name, second_name, email):
    subject = 'Email'
    html_message = render_to_string('email.html', {'name': name, 'second_name': second_name})
    plain_text = strip_tags(html_message)
    from_email = 'From <curze.curze@yandex.ru>'
    to = email

    send_mail(subject, plain_text, from_email, [to], html_message=html_message)
    print(email, html_message, plain_text)


for user in User.access():
    print('send')
    send_email(user.name, user.second_name, user.email)
