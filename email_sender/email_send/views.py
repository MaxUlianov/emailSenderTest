# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from email_send.models import User
from email_send.forms import AddUserForm

from PIL import Image
from django.http import HttpResponse
import logging
import datetime
from django.contrib.sites.models import Site

logger = logging.getLogger(__name__)


def index(request):
    url = request.build_absolute_uri()

    current_site = Site.objects.get_current()
    current_site.domain = url
    current_site.name = 'Site'
    current_site.save()

    form = AddUserForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
        return redirect("email_send_index")

    return render(request, 'index.html', {"form": form})


def image_load(request):
    img = Image.new('RGB', (1, 1))
    response = HttpResponse(content_type="image/png")
    img.save(response, "PNG")

    logging.warning('email opened at {time}'.format(time=datetime.datetime.now()))
    return response
