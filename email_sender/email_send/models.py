# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class User(models.Model):
    name = models.CharField(max_length=25, blank=False)
    second_name = models.CharField(max_length=30, blank=False)
    email = models.CharField(max_length=30, blank=False)

    def __str__(self):
        return self.name + ' ' + self.second_name
