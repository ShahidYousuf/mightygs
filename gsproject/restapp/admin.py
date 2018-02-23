# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from restapp.models import Question, Subject

# Register your models here.

admin.site.register(Question)
admin.site.register(Subject)



