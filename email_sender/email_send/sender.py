from django.core.mail import send_mail
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'email_sender.settings')
django.setup()

from email_send.models import User
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.contrib.sites.models import Site


def get_site():
    return Site.objects.get_current()


def send_email(name, second_name, email):
    subject = 'Email'

    print(get_site())
    # image_url = HttpRequest.build_absolute_uri(reverse("image_load"))
    image_url = r'^image_load/$'

    html_message = render_to_string('email.html', {'name': name, 'second_name': second_name, 'image_url': image_url})
    plain_text = strip_tags(html_message)
    from_email = 'From <curze.curze@yandex.ru>'
    to = email

    send_mail(subject, plain_text, from_email, [to], html_message=html_message)
    print(email, html_message, plain_text)


for user in User.access():
    send_email(user.name, user.second_name, user.email)
