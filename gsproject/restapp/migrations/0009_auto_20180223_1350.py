# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-23 13:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapp', '0008_auto_20180223_1334'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(choices=[('HIST', 'History'), ('GEOG', 'Geography'), ('POLI', 'Polity'), ('SCIE', 'Science'), ('ECON', 'Economics'), ('GENK', 'Gk'), ('ECOL', 'Ecology')], default='HIST', max_length=15)),
            ],
        ),
        migrations.RemoveField(
            model_name='section',
            name='questions',
        ),
        migrations.RemoveField(
            model_name='question',
            name='subject',
        ),
        migrations.AddField(
            model_name='question',
            name='section',
            field=models.CharField(default='section title here', max_length=100),
        ),
        migrations.DeleteModel(
            name='Section',
        ),
        migrations.AddField(
            model_name='subject',
            name='questions',
            field=models.ManyToManyField(related_name='questions', to='restapp.Question'),
        ),
    ]
