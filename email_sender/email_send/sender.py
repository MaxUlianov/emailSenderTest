import logging

from django.core.mail import send_mail
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'email_sender.settings')
django.setup()

from email_send.models import User
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.contrib.sites.models import Site


def send_email(name, second_name, email, content):
    site = Site.objects.get_current()

    # hard-coded image url, if site doesnt work
    # image_url = 'http://192.168.100.36:5000/image_load'
    image_url = str(site) + 'image_load'
    print('image url = ', image_url)

    if content:
        subject = content["subject"]
        template = content["template"]
    else:
        # default email
        subject = 'Email'
        template = 'email.html'

    html_message = render_to_string(template, {'name': name, 'second_name': second_name, 'image_url': image_url})
    plain_text = strip_tags(html_message)
    from_email = 'Sender <curze.curze@yandex.ru>'
    to = email

    send_mail(subject, plain_text, from_email, [to], html_message=html_message)


def send_emails_to_users(content):
    for user in User.access():
        send_email(user.name, user.second_name, user.email, content)


if __name__ == '__main__':
    content = {'template': 'email.html', 'subject': 'Promo Email'}
    send_emails_to_users(content)
