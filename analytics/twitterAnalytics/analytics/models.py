# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class Tweets(models.Model):
    contributors = models.CharField(max_length=200, null = True)
    truncated = models.BooleanField()
    text = models.TextField()
    is_quote_status = models.BooleanField()
    geo = models.CharField(max_length=200, null = True)
    place = models.CharField(max_length=200, null = True)
    created_at = models.DateTimeField()
    timestamp_ms = models.DateTimeField()
    user = models.TextField(max_length=200)