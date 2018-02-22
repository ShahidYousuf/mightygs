# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Question(models.Model):
    text = models.TextField()
    optiona=models.TextField()
    optionb=models.TextField()
    optionc=models.TextField()
    optiond=models.TextField()
    answer=models.CharField(max_length=50)

