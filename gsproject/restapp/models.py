# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Question(models.Model):
    section = models.CharField(max_length=100, default='section title here')
    text = models.TextField()
    a = models.CharField(max_length=40, default='option one')
    b = models.CharField(max_length=40, default='option two')
    c = models.CharField(max_length=40, default='option three')
    d = models.CharField(max_length=40, default='option four')
    answer = models.CharField(max_length=40, default='option five')
    
    def __unicode__(self):
        return self.text


class Subject(models.Model):
    HISTORY = 'HIST'
    GEOGRAPHY = 'GEOG'
    POLITY = 'POLI'
    SCIENCE = 'SCIE'
    ECONOMICS = 'ECON'
    GK = 'GENK'
    ECOLOGY='ECOL'

    SUBJECT_CHOICES = (
     (HISTORY, 'History'),
     (GEOGRAPHY, 'Geography'),
     (POLITY, 'Polity'),
     (SCIENCE, 'Science'),
     (ECONOMICS, 'Economics'),
     (GK, 'Gk'),
     (ECOLOGY, 'Ecology'), 
      )
    subject = models.CharField(max_length=15, choices=SUBJECT_CHOICES, default=HISTORY)
    questions = models.ManyToManyField(Question, related_name='questions')
 
    def __unicode__(self):
        return self.subject



