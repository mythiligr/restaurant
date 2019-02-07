# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Table(models.Model):
    id=models.AutoField(primary_key=True, unique=True)
    name = models.TextField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    # To return model_name
    def __str__(self):
        return self.name

class Booking(models.Model):
    id=models.AutoField(primary_key=True, unique=True)
    table = models.ForeignKey(Table, null=True, on_delete=models.CASCADE)
    booking_time_start = models.TimeField(auto_now_add=False)
    booking_time_end = models.TimeField(auto_now_add=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)